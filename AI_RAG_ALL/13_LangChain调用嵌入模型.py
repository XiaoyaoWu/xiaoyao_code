
from langchain_community.embeddings import DashScopeEmbeddings

model = DashScopeEmbeddings()


print(model.embed_query("香港"))
print(model.embed_documents(["香港","上海","深圳"]))




