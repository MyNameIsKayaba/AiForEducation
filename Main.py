import connect_to_gpt

# User Input
def get_user_info():
    name = input("Hi there! I'm your learning buddy. What's your name? ")
    age = input(f"Nice to meet you, {name}! How old are you? ")
    education = input("What is the highest level of education you have completed? ")
    personality = input("Everyone has something special about them. How would you describe yourself in a few words? ")
    interests = input("What are some things you love doing in your free time? ")
    career = input("Dreaming big is important! What do you want to be when you grow up? ")
    
    return {
        "name": name,
        "age": age,
        "education": education,
        "personality": personality,
        "interests": interests,
        "career": career
    }



def main():
    # user_info = {'name': 'angela', 'age': '6', 'education': '1st grade', 'personality': 'outgoing, curious of everything', 'interests': 'playing video games', 'career': 'top game designer in the world'}
    user_info = get_user_info()
    course_outline = connect_to_gpt.generate_course_outline(user_info) # Connect to GPT
    with open("course_outline.md", 'w') as t:
        t.write(course_outline.choices[0].message.content)
    print(f"course outline saved to course_outline.json for {user_info['name']}")



# Connect to Gamma


if __name__ == "__main__":
    main()