import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(
    model='gpt-4o-mini',
    temperature=0.2
)

template = ChatPromptTemplate.from_messages([
    ('system', 'Você é um vendedor focado no produto {produto}. Seu tom deve ser {tom}.'),
    ('user', 'Como responder à objeção: {objecao}')
])

print('### Enviando para a IA... ###')


cadeia = template | llm
resposta = cadeia.invoke({  
    'produto': 'curso de python',
    'tom': 'entusiasta e persuasivo',
    'objecao': 'Está muito caro'
})


print('\n### RESPOSTA DA IA: ###\n')
print(resposta.content)
