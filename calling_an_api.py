import requests
import json
# import requests_cache  
def request(url, params = {}):
        resp = requests.get(url)
        return resp.json()

url = ' http://saral.navgurukul.org/api/courses'
response = requests.get(url)           
course = json.loads(response.text)
print("**********welcome Navgurukul**************")

id_list= []
print(course)
index=0
while index<len(course["availableCourses"]):
        course_id=course["availableCourses"][index]["id"]
        course_name=course["availableCourses"][index]["name"]
        print(index," ",course_name,"-:",course_id)
        print("-----------------------")
        id_list.append(course_id)
        index=index+1
j=int(input('ENTER THE NUMBER ='))
print("index name : ",course["availableCourses"][j]["name"])
a=course["availableCourses"][j]["id"]
print(a)


exercise_json = request("http://saral.navgurukul.org/api/courses/"+a+"/exercises")
# print(exercise_json)
slug_list = []
index_1=0
while index_1 < len(exercise_json["data"]):
        exercise =exercise_json["data"][index_1]
        exercisename=exercise["name"]
        print(exercisename)
        parent_exercise=exercise["parent_exercise_id"]
        index_1=index_1+1           


        if parent_exercise==None:
                exercise_name=exercise["name"]
                exercise_slug=exercise["slug"]
                slug_list.append(exercise_slug)

                print (str(index_1)+ ". " + exercise_name)
        elif parent_exercise!=None:
                exercise_name=exercise["name"]
                exercise_slug=exercise["slug"]

                slug_list.append(exercise_slug)
                print ("parentexercises",str(index_1)+ ". " + exercise_name)

        index_2=0
        while index_2<len(exercise["childExercises"]):
                child_name=exercise["childExercises"][index_2]["name"]
                child_slug=exercise["childExercises"][index_2]["slug"]
                slug_list.append(child_slug)
                print ("childexercisename: ", str(index_2) + " " + child_name)
                index_2=index_2+1

json_object=json.dumps(exercise_json,indent=4)
with open("course json","w") as outfile:
        outfile.write(json_object)

print("*********************Thanks***************************")


