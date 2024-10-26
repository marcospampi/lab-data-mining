# Homework 1
È stato richiesto di produrre un notebook Jupyter dove, scelto un dataset:
1. Si cercano le prime quattro coppie di feature correlate
2. Si crea il grafico per ognuno di queste coppie.
3. Si computi la PCA e la SVD del dataset, si salvino dunque i risultati su disco.

## Documenti e script prodotti
Sono stati prodotti i seguenti file:
- **homework.ipynb** è il notebook del homework.
- **src/correlator.py** è uno script contenente la classe `Correlator`, cui responsabilità sono:
  - Produrre le combinazioni di coppie di feature.
  - Eseguire i vari metodi di correlazione tramite il metodo `run` e i vari delegati `pearson_fn`, `spearman_fn`, `kendell_fn`.
  - Fondere i dati risultati dalle chiamate al metodo `run` tramite `merge_correlation_results`.
- **src/utils.py** fornisce la funzione `plot_feature_pairs_from_merged_set` per graficare le coppie di feature.

È stato scelto un approccio più funzionale, rispetto ad uno strettamente ad oggetti come richiesto, sia per gusti personali, sia per soggettiva idea che sia più adatto a progetti di piccole dimensioni.

## Librerie utilizzate e dipendenze
- **numpy**
- **matplotlib**
- **scikit-learn**
- **pandas**
- **scipy**

## Difficoltà riscontrate 
Sono state riscontrate una serie di difficoltà nello svolgimento dell'homework:
- La scarsa conoscenza di **pandas** e l'ecosistema di **python** ha portato a rallentamenti generali nello svolgimento dell'homework, dovuti alla necessità di dover continuamente consultare la documentazione ( e Stackoverflow 😅 ).
- Poca sicurezza sulla **PCA** e **SVD**, in particolare come configurare e eseguire le loro implementazioni su **scikit-learn**. Infatti sono stati consultati gli esempi dell'anno precedente.