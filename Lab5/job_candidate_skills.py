job_requirement = {"Python", "Django", "SQL", "Git"}
job_applicant = {"Python", "Flask", "Git", "JavaScript"}

skill_matches = job_requirement & job_applicant
skills_missing = job_requirement - job_applicant
extra_skills = job_applicant - job_requirement

print(f"Matched skills: {list(skill_matches)}")
print(f"Missing skills: {list(skills_missing)}")
print(f"Extra skills: {list(extra_skills)}")

# list = [skills_missing, skill_matches, extra_skills]
# for whatever in list:
#     print(whatever)