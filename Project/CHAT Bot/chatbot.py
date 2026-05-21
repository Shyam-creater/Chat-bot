from flask import Flask
import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.static_folder = 'static'


chatbot = ChatBot(
    'ChatBot for College Enquiry',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "Hi there, Welcome to VTOP! 👋 If you need any assistance, I'm always here.Go ahead and write the number of any query. 😃✨<b><br><br>  Which of the following user groups do you belong to? <br><br> Student's Section Enquiry.</br>Faculty Section Enquiry. </br>Parent's Section Enquiry.</br>Visitor's Section Enquiry.</br> <br>",
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///db.sqlite'   
) 


trainer = ListTrainer(chatbot)




# python app.py
# Training with Personal Ques & Ans 
conversation = [
"Hi",
"How can i help you?",
"Hey",

"How are you?",
"I need help",
"Good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> Student's Section Enquiry.</br>Faculty Section Enquiry. </br>Parent's Section Enquiry.</br>Visitor's Section Enquiry.</br>",

"Great",
"Go ahead and write the number of any query. 😃✨ <br> Student's Section Enquiry.</br>Faculty Section Enquiry. </br>Parent's Section Enquiry.</br>Visitor's Section Enquiry.</br>",

"good",
"Go ahead and write the number of any query. 😃✨ <br> Student's Section Enquiry.</br> Faculty Section Enquiry. </br>Parent's Section Enquiry.</br>Visitor's Section Enquiry.</br>",

"fine",
"Go ahead and write the number of any query. 😃✨ <br> Student's Section Enquiry.</br> Faculty Section Enquiry. </br>Parent's Section Enquiry.</br>Visitor's Section Enquiry.</br>",

"Thank You",
"Your Welcome 😄",

"Thanks",
"Your Welcome 😄",

"Bye",
"Thank You for visiting!..",

"What do you do?",
"I am made to give Information about VTOP Vellore. ",


"What else can you do?",
"I can help you know more about VTOP",
    
    "student",
    "<b>STUDENT <br>The following are frequently searched terms related to student . Please select one from the options below : <br> <br> Curriculars <br>Extra-Curriculars<br> Examination <br> Placements </b>",
    
    "curricular",
    "<b> CURRICULAR <br>  These are the top results: <br> <br> Academic Calendar <br>Moodle <br> Time Table </b>",
    
    "academic calendar",
    "<b >Academic Calendar<br>The link to Academic Calender👉<a href=" 'https://naveendivakar.netlify.app/academic.html' " target="'blank'">Click Here</a> </b>",
    "moodle",
    "<b>Moodle<br>The link to Moodle 👉 <a href=" 'https://moodlestudent.netlify.app/stu_moddle.html' " target="'blank'">Click Here</a> </b>",
    "time table",
    "<b>Time Table<br>The link to Time Table 👉 <a href=" 'https://polite-biscochitos-213f93.netlify.app/college_timetable.html' " target="'blank'">Click Here</a> </b>",
    

    "extra curriculars",
    "<b>EXTRA-CURRICULAR<br>These are the top results: <br> <br>Events<br>Student Chapters <br>Student's Council</b>",
    "events",
    "<b > Events<br>The link to Events👉 <a href=" 'https://naveendivakar.netlify.app/circular_event.html' " target="'blank'">Click Here</a></b>",
    "student chapters",
    "<b > Student Chapters<br>The link to Student Chapters👉<a href=" 'https://naveendivakar.netlify.app/cir_studentchapter.html' " target="'blank'">Click Here</a> </b>",
    "student council",
    "<b >Student's Council <br>The link to Student's Council👉 <a href=" 'https://naveendivakar.netlify.app/cir_studentcouncil.html' " target="'blank'">Click Here</a> </b>",

    "examination" "exam",
    "<b > EXAMINATION <br>These are the top results:<br> Exam Notices <br> Exam Question</b>",
    "exam question",
    "<b > Exam Question<br>The link to Notices👉 <a href=" 'https://examques.netlify.app/prequestion' " target="'blank'">Click Here</a> </b>",
    "exam notices",
    "<b > Exam Notices<br>The link to Notices👉 <a href=" 'https://notices.netlify.app/notices.html' " target="'blank'">Click Here</a> </b>",
    
    "placement",
    "<b > PLACEMENTS These are the top results:<br> Overview <br> Our Recruiters <br> Placement Statistics </b>",
    "overview",
    "<b> Overview<br>The link to Placements👉 <a href=" 'https://naveendivakar.netlify.app/placement_overview.html' " target="'blank'">Click Here</a> </b>",
    "placement statistics",
    "<b > Placement Tracker<br>The link to Placement tracker👉 <a href=" 'https://naveendivakar.netlify.app/placement_statistic.html' " target="'blank'">Click Here</a> </b>",

    "faculty",
    "<b >FACULTY<br>The following are frequently searched terms related to faculty. Please select one from the options below :</br></br> Portals</b>",
    
    "portals",
    "<b > PORTALS These are the top results:<br> Mark Update <br>Faculty Moodle </b>",
    "mark update",
    "<b> Mark Update<br>The link to Mark Update👉<a href=" 'https://facultymarkupdate.netlify.app/faculty.html' " target="'blank'">Click Here</a> </b>",
    "faculty moodle",
    "<b> Moodle<br>The link to Moodle👉<a href="'https://facultymoodle.netlify.app/index.html'" target="'blank'">Click Here</a> </b>",

    "parent",
    "<b> PARENTS <br>The following are frequently searched terms related to Parents. Please select one from the options below : <br> <br> About Us <br> Notices<br> Placements </b> " ,

    "about us",
    "<b > ABOUT US<br>These are the top results:<br> <br> About Vit </b>",
    "about vit",
    "<b >About vit<br>The link to About Vit👉 <a href=" 'https://naveendivakar.netlify.app/about_vit.html' " target="'blank'">Click Here</a> </b>",
    
    "notices",
    "<b > NOTICES<br>These are the top results:<br> <br> Annoucement  </b>",
    "annoucement",
    "<b >annoucement <br>The link to All Notices👉 <a href=" 'https://notices.netlify.app/notices.html' " target="'blank'">Click Here</a> </b>",

    "placement result",
    "<b > PLACEMENTS These are the top results:<br> <br>Placement Detail<br> Placement Contact <br> Placement Tracker </b>",
    "placement detail",
    "<b> Placements<br>The link to Placements👉 <a href=" 'https://naveendivakar.netlify.app/placement_overview.html' " target="'blank'">Click Here</a> </b>",
    "placement tracker",
    "<b > Placement Tracker<br>The link to Placement Tracker👉 <a href=" 'https://naveendivakar.netlify.app/placement_statistic.html' " target="'blank'">Click Here</a> </b>",

    "visitors",
    "<b VISITORS <br>The following are frequently searched terms related to visitors. Please select one from the options below : <br> <br> Visitor detail<br> Programs We Offer </b>",
    
    "vistior detail",
    "<b > ABOUT US<br>These are the top results:<br> <br> About Vit </b>",
    "about vit",
    "<b >About Vit<br>The link to About CRCE👉 <a href=" 'https://naveendivakar.netlify.app/about_vit.html' " target="'blank'">Click Here</a> </b>",
   
    "Programs We Offer",
    "<b > PROGRAMS WE OFFER <br>These are the top results:<br> <br>Application</b>",
    "application",
    "<b >Application<br>The link to Application👉 <a href=" 'https://applicationadmin.netlify.app/index.html' " target="'blank'">Click Here</a> </b>",
   
]


trainer.train(conversation)  
