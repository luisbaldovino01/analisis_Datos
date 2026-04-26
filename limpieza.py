import pandas as pd

def limpiar_dataset(dataset: pd.DataFrame) -> pd.DataFrame:
    dataset_final = dataset.copy()
    
    #eliminar filas con celdas vacias
    dataset_final = dataset_final.dropna()
    dataset_final = dataset_final.reset_index(drop=True)
    
    return dataset_final
    