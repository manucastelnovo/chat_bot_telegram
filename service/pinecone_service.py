import pinecone 

pinecone.init(api_key='f39718d6-40ba-465c-87bc-78678de8bb52', environment='asia-southeast1-gcp') 
index = pinecone.Index('apocalipsis') 

# upsert_response = index.upsert(
#     vectors=[
#         {
#         'id':'vec1', 
#         'values':embedding, 
#         'metadata':{'page_content': text},
#         }
#     ],
#     )