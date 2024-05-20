import os, json
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# load env file
load_dotenv(find_dotenv())
client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"),
)

def generate_course_outline(user_input):
  response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
      {
        "role": "system",
        "content": "You are a consultant who specializes in customizing personal courses for individuals. Please design a suitable course outline based on the user's personal information."
      },
      {
        "role": "user",
        "content":f"""
    The user has provided the following information:
    User's name: {user_input['name']}
    Age: {user_input['age']}
    Education: {user_input['education']}
    Personality: {user_input['personality']}
    Interests: {user_input['interests']}
    Career Goal: {user_input['career']}

    Based on this information, generate a personal education course outline using markdown. Main title should be the purpose of course including student's name, subtitle should be names of each course, including an estimated learning time after each course title.
    template : '# xxx's Customized Course Outline to Become a xxx\n\n## 1. first course title (times to finish first course)\n   - detail in course \n   - detail in course \n   - detail in course\n   - detail in course\n\n## 2. second course title'
    Simply output the outline in the format provided above for easy parsing by the code. There are no restrictions on the number of lines or the content of the titles.
    """
      }
    ],
    temperature=1,
    max_tokens=256, # should add max token in order to get decent output.
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  return response




# def parse_response(response):
#   lines = response.split('\n')
#   outline = []
#   current_module = {}
#   for line in lines:
#     line = line.strip()
#     if line.startswith("# "):
#       main_title = line
#     elif line.startswith('##'):
#         if current_module:
#             outline.append(current_module)
#         title, duration = line[3:].rsplit('(', 1)
#         current_module = {
#             "title": title.strip(),
#             str(duration.split()[1]): int(duration.split()[0]),
#             "topics": []
#         }
#     elif line.startswith('-'):
#         current_module["topics"].append(line[2:].strip())

#   if current_module:
#       outline.append(current_module)

#   with open('course_outline.json', 'w') as f:
#       json.dump({main_title: outline}, f, indent=4)

#   print("Course outline has been saved to course_outline.json")


# template_response = "# Ray's Customized Course Outline to Become a Top Game Designer\n\n## 1. Introduction to Game Design (2 weeks)\n   - History of Video Games\n   - Fundamental Concepts of Game Design\n   - Overview of Game Development Process\n   - Essential Game Design Terminology\n\n## 2. Programming Basics (3 weeks)\n   - Introduction to Computer Programming\n   - Learning Python/Ruby/JavaScript (choose one to start)\n   - Basic Algorithms and Data Structures\n   - Coding Exercises and Projects\n\n## 3. Advanced Game Programming (6 weeks)\n   - Introduction to Game Engines (Unity/Unreal Engine)\n   - Understanding Physics in Games\n   - Game Scripting Fundamentals\n   - Building Simple Games and Prototypes\n\n## 4. Game Art and Animation (4 weeks)\n   - Basics of Digital Art\n   - Introduction to Animation\n   - Using Tools like Photoshop, Blender, Maya\n   - Practical Projects: Create Characters and Environments\n\n## 5. Level Design and World Building (4 weeks)\n   - Principles of Level Design\n   - Creating Engaging Game Worlds\n   - Balancing Challenge and Fun\n   - Case Studies of Popular Games\n\n## 6. Sound Design and Music (3 weeks)\n   - Basics of Sound Design\n   - Using Audio Software (Audacity, FL Studio)\n   - Creating Sound Effects and Music for Games\n   - Integrating Sound into Game Projects\n\n## 7. Storytelling and Narrative Design (3 weeks)\n   - Elements of Storytelling in Games\n   - Designing Compelling Characters and Plots\n   - Writing Interactive Narratives\n   - Case Studies of Story-Driven Games\n\n## 8. User Interface (UI) and User Experience (UX) Design (3 weeks)\n   - Introduction to UI/UX\n   - Principles of Good UI Design\n   - Prototyping and Wireframing\n   - Testing and Iteration\n\n## 9. Game Testing and Quality Assurance (2 weeks)\n   - Basics of Game Testing\n   - Identifying and Reporting Bugs\n   - Playtesting Techniques\n   - Polishing and Refining Games\n\n## 10. Marketing and Business of Games (2 weeks)\n   - Introduction to Game Marketing\n   - Monetization Strategies\n   - Understanding Game Publishing\n   - Networking and Branding\n\n## 11. Portfolio Development (2 weeks)\n   - Building an Online Portfolio\n   - Showcasing Projects and Skills\n   - Resume and Cover Letter Writing\n   - Interview"
# if __name__ == "__main__":
#   parse_response(template_response)