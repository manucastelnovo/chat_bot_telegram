
import pinecone 
​
pinecone.init(api_key='YOUR_API_KEY', environment='us-east1-gcp') 
index = pinecone.Index('example-index') 
​
upsert_response = index.upsert(
    vectors=[
        {
        'id':'vec1', 
        'values':[0.1, 0.2, 0.3, 0.4], 
        'metadata':{'genre': 'drama'},
           'sparse_values':
           {'indices': [10, 45, 16],
           'values':  [0.5, 0.5, 0.2]}
           }]
