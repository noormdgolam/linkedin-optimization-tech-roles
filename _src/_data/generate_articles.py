import json
import os

DATA_DIR = os.path.dirname(os.path.abspath(__file__))

articles = []

# 10 Pillar Articles
pillar_titles = [
    "The Ultimate Guide to LinkedIn Optimization for Software Engineers",
    "How to Write a Technical LinkedIn Summary That Attracts Recruiters",
    "LinkedIn Headline Strategies for Data Scientists and Analysts",
    "Networking on LinkedIn: A Tech Professional's Masterclass",
    "Showcasing GitHub and Portfolio Links on Your LinkedIn Profile",
    "How Product Managers Can Optimize Their LinkedIn Profiles",
    "Keyword Optimization for Tech Jobs on LinkedIn",
    "Using LinkedIn Creator Mode as a Tech Leader",
    "The Role of LinkedIn Recommendations in Tech Hiring",
    "LinkedIn Job Search Strategies for US Remote Tech Roles"
]

categories = [
    "Profile Optimization", "Profile Optimization", "Profile Optimization", 
    "Networking", "Portfolio & Projects", "Profile Optimization", 
    "Job Search", "Personal Branding", "Networking", "Job Search"
]

for i in range(10):
    title = pillar_titles[i]
    slug = title.lower().replace(' ', '-').replace("'", "").replace(',', "").replace(":", "")
    articles.append({
        "title": title,
        "slug": slug,
        "category": categories[i],
        "date": "2026-07-13",
        "description": f"Learn the best practices and actionable tips for {title.lower()} to boost your career in the tech industry.",
        "content_md": f"## Introduction\n\nWelcome to the comprehensive guide on **{title}**. In the highly competitive US tech job market, having a strong LinkedIn presence is no longer optional—it's essential.\n\n### Key Takeaways\n- Actionable steps to improve your visibility.\n- How recruiters search for tech talent.\n- Strategies to stand out among thousands of applicants.\n\n## Why It Matters\n\nOptimizing your profile ensures that recruiters and hiring managers find you when they search for specific skills like Python, React, Data Analysis, or Cloud Computing.\n\n### Step-by-Step Optimization\n1. **Use a Professional Photo:** A clean, friendly headshot.\n2. **Craft a Compelling Headline:** Don't just list your job title.\n3. **Detail Your Experience:** Focus on impact and metrics.\n\n## Conclusion\n\nBy following these strategies, you'll be well on your way to maximizing your LinkedIn potential.\n\n## FAQs\n\n**Q: How often should I update my LinkedIn?**\nA: At least once a quarter, or whenever you learn a new skill.\n\n**Q: Should I pay for LinkedIn Premium?**\nA: It can be helpful for direct messaging recruiters, but a well-optimized free profile is powerful enough for most."
    })

# 90 Placeholder Articles
for i in range(1, 92):
    title = f"Actionable LinkedIn Tip #{i} for Tech Roles"
    slug = f"actionable-linkedin-tip-{i}-for-tech-roles"
    articles.append({
        "title": title,
        "slug": slug,
        "category": "Quick Tips",
        "date": "2026-07-12",
        "description": f"Quick and actionable tip number {i} to optimize your LinkedIn profile and land your dream tech job.",
        "content_md": f"## Tip #{i}\n\nThis is a quick, actionable tip for tech professionals looking to improve their LinkedIn presence.\n\n### How to apply it\nMake sure to review your profile settings and implement this change today to see an increase in search appearances.\n\n## Conclusion\nSmall tweaks can lead to big results over time."
    })

with open(os.path.join(DATA_DIR, 'articles.json'), 'w', encoding='utf-8') as f:
    json.dump(articles, f, indent=2)

print(f"Generated {len(articles)} articles.")
