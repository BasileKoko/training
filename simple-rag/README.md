Simple `RAG`

### Architecture Overview
The RAG pipeline has 3 main stages:

Document Ingestion — Load and chunk your data
Embedding + Retrieval — Convert chunks into vectors and store for similarity search
Augmented Generation — Fetch relevant chunks and pass them to the LLM for response


![rag_architecture.png](rag_architecture.png)


### Run the project in Docker

1- Build the image
```
docker build -t simple-rag .
```
2- Run the image

```
docker run -it --rm \
  --env-file .env \
  -v "$(pwd)/chroma_db:/app/chroma_db" \
  simple-rag
```
3- Examples of the questions and response generated

```
Ask a question: do you know anything about parental leave?

Answer:
Yes, according to the provided documents, parental leave at Aetheria Dynamics is structured as follows:

*   **Primary caregivers:** Eligible for 16 weeks of 100% paid leave following the birth or adoption of a child.
*   **Secondary caregivers:** Eligible for 6 weeks of 100% paid leave.
*   **Eligibility requirement:** Employees must be employed at Aetheria Dynamics for at least 6 months prior to the event to qualify.

Ask a question: what about health and safety

Answer:
Based on the provided documents, health and safety responsibilities are structured as follows:

**Management and Oversight:**
*   Resources must be allocated to maintain workplace safety standards.
*   The Corporate Health & Safety Committee (CHSC) is responsible for conducting quarterly safety audits and reviewing incident reports.
*   Full compliance with applicable occupational health and safety regulations must be ensured.

**Department Managers & Team Leads:**
*   Must ensure all new hires and contractors complete mandatory safety onboarding before accessing workspaces or equipment.
*   Must enforce daily adherence to Personal Protective Equipment (PPE) requirements and operational Standard Operating Procedures (SOPs).
*   Must promptly investigate and document all workplace hazards, near-misses, and injuries within their teams.

**Employees & Contractors:**
*   Must follow all posted safety instructions, equipment manuals, and emergency procedures.
*   Must immediately report unsafe conditions, damaged equipment, or suspicious activity to a supervisor or the Safety Desk.
*   Must refrain from operating specialized machinery, high-voltage systems, or chemical agents without documented certification.

Ask a question: give me details of salary

Answer:
Based on the provided documents, salary adjustments (merit increases) are determined during the December cycle and take effect on February 1st of the following year.
```
