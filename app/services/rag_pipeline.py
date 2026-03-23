from langchain_community.llms import Ollama
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from app.services.vector_store import get_vector_store

# Load LLM
llm = Ollama(model="llama3")

# Load vector DB
vector_store = get_vector_store()
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

# ---------------- PROMPT ----------------
system_prompt = (
    "You are a Medical AI Assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer the question. "
    "If you don't know the answer, say that you don't know. "
    "Use three sentences maximum and keep the answer concise.\n\n"
    "{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

# Chain 
question_answer_chain = create_stuff_documents_chain(llm, prompt)

rag_chain = create_retrieval_chain(retriever, question_answer_chain)

custom_qa = {

    "hello": "Hello, I am your medical assistant. Please ask about medical topics like acne, diabetes or fever.",
    "what is acne": "According to the provided context, acne is a common skin disease characterized by pimples on the face, chest, and back, caused by clogged pores with oil, dead skin cells, and bacteria. It's also known as acne vulgaris, which is the medical term for common acne.",
    
    "diabetes": "Diabetes is a chronic condition that affects how your body processes blood sugar (glucose), leading to high blood sugar levels.",
    
    "what is fever": "Fever is a temporary increase in body temperature, often due to an illness or infection.",
    
    "blood pressure": "Blood pressure is the force of blood pushing against the walls of arteries as the heart pumps blood.",

    "how to treat acne": "Acne can be treated with proper skincare, including cleansing, avoiding oily products, and using medications like benzoyl peroxide or salicylic acid.",

    "acne symptoms": "Symptoms of acne include pimples, blackheads, whiteheads, and sometimes painful cysts on the skin.",

    "diabetes symptoms": "Common symptoms include increased thirst, frequent urination, fatigue, and blurred vision.",
    "diabetes treatment": "Treatment includes a healthy diet, regular exercise, blood sugar monitoring, and medication or insulin if needed.",
    
    "fever symptoms": "Symptoms include high temperature, sweating, chills, headache, and weakness.",
    "how to treat fever": "Treatment includes rest, drinking fluids, and taking medications like paracetamol if necessary.",

    "what is headache": "A headache is pain or discomfort in the head or neck region.",
    "headache causes": "Causes include stress, dehydration, lack of sleep, or medical conditions like migraines.",
    "headache treatment": "Treatment includes rest, hydration, and pain relievers like ibuprofen.",

    "what is cold": "The common cold is a viral infection affecting the nose and throat.",
    "cold symptoms": "Symptoms include runny nose, sore throat, cough, and sneezing.",
    "cold treatment": "Treatment includes rest, fluids, and over-the-counter medications.",


    "what is cough": "A cough is a reflex action to clear the airways of mucus or irritants.",
    "cough causes": "Causes include infections, allergies, or respiratory conditions.",
    "cough treatment": "Treatment depends on the cause and may include cough syrups or home remedies.",

    "what is allergy": "An allergy is an immune system reaction to a foreign substance.",
    "allergy symptoms": "Symptoms include sneezing, itching, rash, and swelling.",
    "allergy treatment": "Treatment includes avoiding allergens and taking antihistamines.",

    "what is asthma": "Asthma is a chronic condition that affects the airways in the lungs.",
    "asthma symptoms": "Symptoms include wheezing, shortness of breath, and chest tightness.",
    "asthma treatment": "Treatment includes inhalers and avoiding triggers.",

    "what is heart disease": "Heart disease refers to conditions affecting the heart.",
    "heart disease symptoms": "Symptoms include chest pain, shortness of breath, and fatigue.",
    "heart disease treatment": "Treatment includes lifestyle changes, medication, or surgery.",

    "what is stomach pain": "Stomach pain refers to discomfort in the abdominal area.",
    "stomach pain causes": "Causes include indigestion, infection, or gastrointestinal issues.",
    "stomach pain treatment": "Treatment depends on cause and may include medication or diet changes.",

    "what is flu": "Flu is a viral infection that affects the respiratory system.",
    "flu symptoms": "Symptoms include fever, chills, body aches, and fatigue.",
    "flu treatment": "Treatment includes rest, fluids, and antiviral medications if needed.",

    "what is migraine": "Migraine is a neurological condition causing intense headaches.",
    "migraine symptoms": "Symptoms include severe headache, nausea, and sensitivity to light.",
    "migraine treatment": "Treatment includes medication, rest, and avoiding triggers.",

    "what is skin infection": "A skin infection occurs when harmful bacteria or fungi infect the skin.",
    "skin infection symptoms": "Symptoms include redness, swelling, pain, and pus.",
    "How to treat skin infection" or "skin infection treatment": "Treatment includes antibiotics or antifungal medications.",

    "what is dehydration": "Dehydration occurs when your body loses more fluids than it takes in.",
    "dehydration symptoms": "Symptoms include dry mouth, dizziness, and dark urine.",
    "dehydration treatment": "Treatment includes drinking fluids and electrolyte solutions.",

}

def get_response(question: str):
    q = question.lower().strip()

    # Step 1: Check predefined answers
    for keyword in custom_qa:
        if keyword in q:
            return custom_qa[keyword]

    # Step 2: fallback (optional)
    try:
        response = rag_chain.invoke({"input": question})
        return response["answer"]
    except:
        return "I'm a medical assistant. Please ask about common medical topics like acne, diabetes, or fever."