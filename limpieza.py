import pandas as pd

def limpiar_dataset(dataset: pd.DataFrame) -> pd.DataFrame:
    dataset_copia = dataset.copy()
    
    #eliminar filas con celdas vacias
    dataset_copia = dataset_copia.dropna()
    dataset_copia = dataset_copia.reset_index(drop=True)
    
    #eliminar columnas innecesarias
    columnas_eliminar = ["COLE_CALENDARIO", "COLE_COD_DANE_ESTABLECIMIENTO", "COLE_COD_DANE_SEDE", "COLE_COD_DEPTO_UBICACION", "COLE_COD_MCPIO_UBICACION", "ESTU_COD_DEPTO_PRESENTACION", "ESTU_COD_MCPIO_PRESENTACION", "ESTU_COD_RESIDE_DEPTO", "ESTU_COD_RESIDE_MCPIO", "ESTU_CONSECUTIVO", "COLE_CODIGO_ICFES"]
    
    dataset_copia = dataset_copia.drop(columns=columnas_eliminar)
    
    
    return dataset_copia
    