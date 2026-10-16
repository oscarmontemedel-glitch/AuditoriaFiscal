#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extractor local de CFDI XML para revisión preliminar. No determina impuestos definitivos."""
import argparse, csv, hashlib, sys
from pathlib import Path
import xml.etree.ElementTree as ET
from decimal import Decimal, InvalidOperation
NS={'cfdi':'http://www.sat.gob.mx/cfd/4'}
COLS=['ArchivoXML','UUID','Fecha','TipoDeComprobante','Moneda','TipoCambio','MetodoPago','FormaPago','RFCEmisor','NombreEmisor','RFCReceptor','NombreReceptor','UsoCFDI','Subtotal','Descuento','Total','IVA16','IVA8','IVA0_Base','IVA_Exento_Base','IVA_Retenido','ISR_Retenido','IEPS','EstatusCFDI','EfectoFiscalManual','FechaCobroPago','DeducibleManual','AcreditableManual','CuentaCargo','CuentaAbono','DescripcionPoliza','Observaciones','SHA256']
def d(x):
 try:return Decimal(x or '0')
 except (InvalidOperation,ValueError):return Decimal(0)
def a(n,k,default=''):return n.attrib.get(k,default) if n is not None else default
def tax(root,imp,ret=False,rate=None,base=False):
 total=Decimal(0); path='.//cfdi:Retencion' if ret else './/cfdi:Traslado'
 for n in root.findall(path,NS):
  if a(n,'Impuesto')!=imp:continue
  if rate is not None and (a(n,'TasaOCuota')!=rate):continue
  total+=d(a(n,'Base' if base else 'Importe'))
 return str(total)
def parse(p):
 raw=p.read_bytes(); sha=hashlib.sha256(raw).hexdigest()
 try:r=ET.fromstring(raw)
 except ET.ParseError as e:return {'ArchivoXML':p.name,'Observaciones':f'XML inválido: {e}','SHA256':sha}
 def local(parent,name):return next((x for x in list(parent or []) if x.tag.rsplit('}',1)[-1]==name),None)
 em=local(r,'Emisor'); rec=local(r,'Receptor'); comp=local(r,'Complemento'); uuid=''
 if comp is not None:
  for x in comp.iter():
   if x.tag.rsplit('}',1)[-1]=='TimbreFiscalDigital':uuid=a(x,'UUID');break
 tipo=a(r,'TipoDeComprobante'); obs=[]
 if not uuid:obs.append('UUID no localizado')
 if tipo=='P':obs.append('Complemento de pago: aplicar contra CFDI origen; no duplicar ingreso/gasto')
 if a(r,'Moneda','MXN') not in ('MXN','XXX') and not a(r,'TipoCambio'):obs.append('Revisar tipo de cambio aplicable')
 ex=Decimal(0)
 for x in r.findall('.//cfdi:Traslado',NS):
  if a(x,'Impuesto')=='002' and a(x,'TipoFactor')=='Exento':ex+=d(a(x,'Base'))
 return {'ArchivoXML':p.name,'UUID':uuid,'Fecha':a(r,'Fecha'),'TipoDeComprobante':tipo,'Moneda':a(r,'Moneda','MXN'),'TipoCambio':a(r,'TipoCambio'),'MetodoPago':a(r,'MetodoPago'),'FormaPago':a(r,'FormaPago'),'RFCEmisor':a(em,'Rfc'),'NombreEmisor':a(em,'Nombre'),'RFCReceptor':a(rec,'Rfc'),'NombreReceptor':a(rec,'Nombre'),'UsoCFDI':a(rec,'UsoCFDI'),'Subtotal':a(r,'SubTotal'),'Descuento':a(r,'Descuento'),'Total':a(r,'Total'),'IVA16':tax(r,'002',rate='0.160000'),'IVA8':tax(r,'002',rate='0.080000'),'IVA0_Base':tax(r,'002',rate='0.000000',base=True),'IVA_Exento_Base':str(ex),'IVA_Retenido':tax(r,'002',ret=True),'ISR_Retenido':tax(r,'001',ret=True),'IEPS':tax(r,'003'),'EstatusCFDI':'No verificado contra SAT','EfectoFiscalManual':'Por revisar','FechaCobroPago':'','DeducibleManual':'Por revisar','AcreditableManual':'Por revisar','CuentaCargo':'','CuentaAbono':'','DescripcionPoliza':f'CFDI {tipo} {uuid or p.stem}','Observaciones':'; '.join(obs),'SHA256':sha}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('carpeta',type=Path);ap.add_argument('-o','--salida',type=Path,default=Path('cfdi_extraidos.csv'));args=ap.parse_args()
 if not args.carpeta.is_dir():print('La ruta no es una carpeta',file=sys.stderr);return 2
 files=sorted(set(list(args.carpeta.rglob('*.xml'))+list(args.carpeta.rglob('*.XML'))))
 if not files:print('No se encontraron XML',file=sys.stderr);return 1
 rows=[parse(p) for p in files];counts={}
 for r in rows:
  u=r.get('UUID','')
  if u:counts[u]=counts.get(u,0)+1
 for r in rows:
  if r.get('UUID') and counts[r['UUID']]>1:r['Observaciones']=(r.get('Observaciones','')+'; UUID duplicado; revisar').strip('; ')
 args.salida.parent.mkdir(parents=True,exist_ok=True)
 with args.salida.open('w',newline='',encoding='utf-8-sig') as f:w=csv.DictWriter(f,fieldnames=COLS,extrasaction='ignore');w.writeheader();w.writerows(rows)
 print(f'XML leídos: {len(files)}; CSV: {args.salida.resolve()}');print('Extracción técnica únicamente; revisar vigencia SAT, pagos, deducciones, acreditamiento, régimen y retenciones.')
if __name__=='__main__':raise SystemExit(main())
