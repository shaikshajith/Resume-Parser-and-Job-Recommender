def missing_keywords(resume_text, job_desc_text):
    resume_tokens = set(resume_text.split())
    job_tokens = set(job_desc_text.split())
    return list(job_tokens - resume_tokens)
