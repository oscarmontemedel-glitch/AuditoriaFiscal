# Herramienta CFDI XML — ISR, IVA y pólizas

Kit auxiliar para extracción local de CFDI en México. Incluye una calculadora Excel para concentrar XML, resúmenes preliminares de IVA e ISR y propuestas de pólizas, más un script Python para extraer campos a CSV.

## Aviso de alcance
La herramienta produce controles preliminares, no una determinación fiscal definitiva. El XML por sí solo no acredita pago/cobro efectivo, materialidad, deducibilidad, acreditamiento, estatus SAT ni procedencia de retenciones. Validar régimen fiscal, complementos de pago, cancelaciones/sustituciones, tipo de cambio, requisitos de LISR/LIVA/CFF y disposiciones aplicables al periodo.

## Archivos del kit
- `procesar_cfdi.py`: extractor local de XML a CSV UTF-8-SIG.
- `Calculadora_Fiscal_XML_ISR_IVA_Polizas.xlsx`: libro Excel con hojas `INICIO`, `CFDI`, `RESUMEN_IVA`, `RESUMEN_ISR`, `POLIZAS` y `NORMATIVA`.

## Ejecución
`python procesar_cfdi.py ./xml_recibidos -o recibidos.csv`

Importa el CSV a la hoja `CFDI` y revisa manualmente el tratamiento fiscal, las cuentas contables y la partida doble antes de usar las pólizas.

## Fuentes oficiales
- SAT CFDI/Anexo 20: https://www.sat.gob.mx/minisitio/Factura/emite_materialdeayudaparafactura.htm
- RMF y anexos 2026: https://wwwnp.sat.gob.mx/minisitio/NormatividadRMFyRGCE/normatividad_rmf_rgce2026.html
- CFF: https://www.diputados.gob.mx/LeyesBiblio/pdf/CFF.pdf
- LIVA: https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf
- Leyes federales (consultar LISR vigente): https://www.diputados.gob.mx/LeyesBiblio/

No subir XML/CSV con datos fiscales reales a un repositorio público. Mantener los originales en un entorno autorizado y restringido.
