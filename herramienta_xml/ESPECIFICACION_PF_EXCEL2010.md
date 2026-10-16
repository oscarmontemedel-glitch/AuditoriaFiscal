# Especificación — Personas físicas, CFDI emitidos/recibidos y Excel 2010

## Flujo
1. Extraer CFDI a nivel documento y complementos de pago a nivel relación DocumentoRelacionado.
2. Identificar UUID duplicados y separar CFDI tipo I/E/P/N/T.
3. Relacionar CFDI tipo P con UUID original, parcialidad, monto pagado y saldo insoluto; no volver a reconocer el total del CFDI origen desde el complemento.
4. Conciliar contra bancos y auxiliares; capturar fecha efectiva de cobro/pago, régimen PF, deducibilidad, acreditamiento, estatus SAT y cuentas.
5. Preparar cédula mensual separada por régimen y actividad. No usar una tarifa única de ISR para todas las personas físicas.
6. Generar propuesta de póliza y exigir que cargos = abonos antes de exportar/importar.

## Compatibilidad
Excel 2010: usar SUMAR.SI.CONJUNTO, SI, SUMA, INDICE, COINCIDIR y BUSCARV. Evitar BUSCARX, LET, FILTRAR, UNICOS, SECUENCIA, macros y funciones de matriz dinámica.

## Controles fiscales obligatorios
- CFDI: cotejar vigencia/cancelación ante SAT, RFC, fechas, uso, régimen, tipo, moneda y relaciones de sustitución.
- ISR PF: clasificar actividad empresarial/servicios profesionales, arrendamiento, RESICO, salarios y demás ingresos; aplicar reglas y tarifas del régimen y periodo, con deducciones autorizadas y retenciones procedentes.
- IVA: separar tasa 16%, 8%, 0%, exento, no objeto y retenciones. El acreditamiento requiere analizar pago efectivo y requisitos de la LIVA.
- Complemento de pago: conciliar pagos parciales, moneda y equivalencia; evitar doble conteo del CFDI origen.
- Pólizas: catálogo editable, cuentas configurables, moneda/tipo de cambio documentado, folio de póliza y validación de partida doble.

## Fuentes oficiales
- RMF 2026 y anexos: https://wwwnp.sat.gob.mx/minisitio/NormatividadRMFyRGCE/normatividad_rmf_rgce2026.html
- CFDI/Anexo 20: https://www.sat.gob.mx/minisitio/Factura/emite_materialdeayudaparafactura.htm
- Complemento de pagos: https://wwwmat.sat.gob.mx/consultas/92764/comprobante-de-recepcion-de-pagos
- LISR/LIVA: https://wwwmat.sat.gob.mx/normatividad/50768/leyes

Esta herramienta es una cédula de trabajo y no una opinión fiscal ni una declaración automática. El XML por sí solo no acredita pago/cobro, materialidad, deducibilidad, acreditamiento ni estatus vigente ante SAT.