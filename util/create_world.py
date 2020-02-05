from django.contrib.auth.models import User
from adventure.models import Player, Room


Room.objects.all().delete()

orientation = Room(title="First day of school",
              description="To the North, the Web awaits. To the West, the DS awaits. To the East, the IOS awaits. To the South, the UX awaits.")

web_1 = Room(title="User Interface", description="Ability to craft a user interface, a key skill for web developers")

web_2 = Room(title="Advanced CSS", description="Responsive design pushes our basic CSS styling forward for thousands of devices")

web_3 = Room(title="JavaScript Fundamentals", description="JS is fundamental to web development, without it, there is no web")

web_4 = Room(title="Applied JavaScript", description="Applying your JS knowledge to the Document Object Model and creating rich JS UIs.")

web_5 = Room(title="Intro to React", description="React is a UI library that is used in various forms to create complex, rich user interfaces.")

web_6 = Room(title="Single Page Applications", description="Modern applications are built where React App and server are separated out into their own concepts.")

web_7 = Room(title="Advanced React", description="Class Components, React lifecycle, Testing Web Apps.")

web_8 = Room(title="Advanced State Management", description="Context API, Reducer Pattern, Redux, Async Redux.")

web_9 = Room(title="Advanced Web Applications", description="Testing React, Client-Side Auth, AJAX, Deploying Web Apps.")

web_10 = Room(title="Delivering a Single Page App", description="You will be a Front-End Architect, show off your skills!")

web_10b_node = Room(title="Build a Web API", description="Web services based on the REST (REpresentational State Transfer) architecture.")
web_10b_java = Room(title="WEB Java Fundamentals", description="Learning the Java fundamentals and its emphasis on API programming")

web_11_node = Room(title="Adding Data Persistence", description="Databases are ubiquitous in just about everything we do.")
web_11_java = Room(title="Java with RDBMS and API Introduction", description="Web APIs using Java and the Spring Framework and connecting those to a PostgreSQL database")

web_12_node = Room(title="Authentication and Testing", description=" Auth ties in the principles of Server Sessions Password Encryption/Hashing Security Risks.")
web_12_java = Room(title="Java Frameworks", description="Enhancing our Web APIs with exception handling, paging, caching, testing, and finally deployment.")

web_13_node = Room(title="Node Build", description="Build a Node Backend API")
web_13_java = Room(title="Java Build", description="Build a Java Backend API!")

web_13b_reconvene = Room(title="BackEnd Reunion", description="Get back together with your friends!")

web_14 = Room(title="Career Lecture", description="Learn what exactly goes into Lambda School's career endorsement project")

ds_1 = Room(title="Exploratory Data Analysis", description="Cover the Lambda School Data Science Github workflow and assignment submission process.")

ds_2 = Room(title="Make Features", description="At the end of this module, you should be able to understand the purpose of feature engineering.")

ds_3 = Room(title="Join and Reshape Data", description="Preparing data isn’t just about importing it and imputing missing values. ")

ds_4 = Room(title="Make Explanatory Visualizations", description="Identify misleading visualizations, utilize basic matplotlib terminology.")

ds_5 = Room(title="Probability, Statistics, and Inference", description="Statistics accepts situations where the exact and complete are unattainable.")

ds_6 = Room(title="Sampling, Confidence Intervals, and Hypothesis Testing", description="Sampling and other key topics related to sampling such as confidence intervals and hypothesis testing.")

ds_7 = Room(title="Introduction to Bayesian Inference", description="Frequentist statistics is well-established, and is still the default in most situations.")

ds_8 = Room(title="Vectors and Matrices", description="Fundamentals of linear algebra is critical in order to be a well-rounded data scientist.")

ds_9 = Room(title="Intermediate Linear Algebra", description="Review of some basic statistics concepts: Variance, Standard Deviation, Covariance, Correlation.")

ds_10 = Room(title="Dimensionality Reduction Techniques", description="Introduction to: Vector transformations, Eigenvectors and Eigenvalues, The “Curse of Dimensionality.”")

ds_11 = Room(title="Clustering", description="IGeneral overview for the different categories of Machine Learning Algorithms.")

ds_12 = Room(title="Regression 1", description="Here you will begin with baselines for regression.")

ds_13 = Room(title="Regression 2", description="Learn to do train/test split regressions.")

ds_14 = Room(title="Ridge Regression", description="Soon you will be able to do one-hot encoding of categorical features.")

ds_15 = Room(title="Logistic Regression", description="Here you will learn to do train/validate/test split.")

ds_16 = Room(title="Decision Trees", description="In this module you'll learn to clean data with outliers and missing values.")

ds_17 = Room(title="Random Forests", description="By now you should be able to use scikit-learn for random forests.")

ds_18 = Room(title="Cross-Validation", description="Here you will do cross-validation with independent test set.")

ds_19 = Room(title="Classification Metrics", description="You will get and interpret the confusion matrix for classification models.")

ds_20 = Room(title="Applied Modeling", description="You will publish a web app or blog post with visualizations to explain your model.")

ux_1 = Room(title="UX Fundamentals", description="..this is an intro to the world of UX..")
ux_2 = Room(title="Discovery", description="..this is where reseach is made..")

ux_3 = Room(title="Identifying and Organizing Problems", description="..your observational skills will be tested")
ux_4 = Room(title="Personas", description="..you will learn how to use persona/proto-persona..")
ux_5 = Room(title="Journey Maps", description="..you will create a journey map..")
ux_6 = Room(title="User Flows", description="..user flows will be used here..")
ux_7 = Room(title="UX Problem Solving", description="..you will be tested in problem solving..")
ux_8 = Room(title="Simple Prototyping", description="..simple planning leads to great products..")
ux_9 = Room(title="Testing Usability and Research", description="..build user experience..")
ux_10 = Room(title="Intro to Design Theory", description="..delve into the theory of design..")
ux_11 = Room(title="High Fidelity Design", description="..tune up your design..")
ux_12 = Room(title="Design Collaboration", description="..learn how to work with others..")
ux_13 = Room(title="Communication building skills", description="..communicate skills will be built here..")
ux_14 = Room(title="UX Portfolio Building", description="..build you portfolio here..")
ux_15 = Room(title="Intro to HTML", description="..learn HTML fundamentals..")
ux_16 = Room(title="Intro to CSS", description="..learn CSS fundamentals..")
ux_17 = Room(title="Responsive CSS", description="..CSS responsive design is key..")
ux_18 = Room(title="CSS Frameworks", description="..the different frameworks..")
ux_19 = Room(title="Intro to HTML and CSS Sprint Challenge", description="..test your HTML and CSS skills..")
ux_20 = Room(title="UX Unit Build", description="..test your UX skills..")

ios_1 = Room(title="Swift Fundamentals", description="..primary language used to build iOS, macOS apps...")
ios_2 = Room(title="iOS Fundamentals I", description="..This Sprint introduces fundamental technologies and concepts used to create basic iOS apps.")
ios_3 = Room(title="iOS Fundamentals II", description="..This sprint expands upon the fundamental concepts you’ve already learned.. ")
ios_4 = Room(title="iOS Unit 1 Build", description="...Build Week Begins for iOS...")
ios_5 = Room(title="iOS Networking Basics", description="..communicate with internet servers using REST and JSON..")
ios_6 = Room(title="iOS User Interface", description="..you’ll learn how to create and customize user interfaces..")
ios_7 = Room(title="Core Data", description="..implement sophisticated model functionality without writing a ton of code..")
ios_8 = Room(title="iOS Unit 2 Build", description="..Build Week 2 Begins for iOS..")
ios_9 = Room(title="Intermediate Swift", description="..we’ll dive deeper into some Swift programming topics including more advanced uses of Codable..")
ios_10 = Room(title="iOS Code Quality", description="..you’ll learn how to do debugging and write unit tests..")
ios_11 = Room(title="Modularity", description="..you’ll learn techniques for keeping code well-factored and modular..")
ios_12 = Room(title="iOS Unit 3 Build", description="..Build Week 3 Begins for iOS..")
ios_13 = Room(title="iOS Media Programming", description="..you’ll learn how to use media in your iOS apps...")
ios_14 = Room(title="Objective-C Part 1", description="..you’ll learn the fundamentals of Objective-C, and will use it to write iOS apps..")
ios_15 = Room(title="Objective-C Part 2", description="..you’ll dive deeper into Objective-C..")
ios_16 = Room(title="Swift and ObjC Interoperability", description="..you have to use a bridging header to expose your Objective-C code to Swift..")
ios_17 = Room(title="KVO/KVC", description="..you will understand and explain Key Value Coding..")
ios_18 = Room(title="Memory Management", description="..you'll learn the rules of manual reference counting..")
ios_19 = Room(title="Cocoa Design Paterns in ObjC", description="..Designing cocoa for iOS..")
ios_20 = Room(title="iOS Unit 4 Build", description="..you'll understand and implement the singleton design pattern in Objective-C..")


labs_1 = Room(title="Release Cycle 1", description="Get your first real product version out!")
labs_2 = Room(title="Release Cycle 2", description="Get your second real product version out!")
labs_3 = Room(title="Stakeholder not happy", description="Stakeholder changes project direction!")
labs_4 = Room(title="Crunch Time", description="Crunch to make Stakeholder changes")

cs_1 = Room(title="Intro to Python and OOP", description=" Python programming language and the basics of the Object-Oriented Programming (OOP).")
cs_2 = Room(title="Algorithms", description="Think about and solve algorithmic problems and analyze the time complexity.")
cs_3 = Room(title="Data Structures", description="Fundamental data structures, including linked lists, queues, and binary search trees.")
cs_4 = Room(title="CS Unit 1 Build", description="Build an interactive Multi-User Dungeon")
cs_5 = Room(title="Hash Tables and Blockchain", description="Hash Tables speediest structures that we’ll study as well as Blockchain, the basis for many cryptocurrencies.")
cs_6 = Room(title="Graphs", description="How to implement graphs, and several of the algorithms surrounding graphs.")
cs_7 = Room(title="Computer Architecture", description="Explore how computers work at a very low level.")
cs_8 = Room(title="CS Unit 2 Build", description="Lambda Treasure Hunt!")

career_readiness_1 = Room(title="Job Search Strategy", description="Learn Job Search Strategies")
career_readiness_2 = Room(title="Interview/Star Stories", description="Creating an Interview story")
career_readiness_3 = Room(title="Interview Etiquette/Strategies", description="Interview Strategies")
career_readiness_4 = Room(title="Endorsement", description="Get Lambda Endorsed!")
lambda_next = Room(title="School Support", description="Support you while job searching")

job_yay = Room(title="GOT THAT JOB", description="ALL DAT MONEY")
ux_yay = Room(title="GOT THAT JOB", description="MAKING DAT MONEY")
hired = Room(title="#hired", description="..You finally posted in the hired channel")
isa_payment = Room(title="ISA Payment", description="make your first ISA payment with your new job")
vacation = Room(title="Vacation", description="..you take a well deserved break after being in Lambda..")
thankful = Room(title="Thankful", description="..become grateful for Lambda...")

#save orientation
orientation.save()
#save web
web_1.save()
web_2.save()

web_3.save()
web_4.save()
web_5.save()
web_6.save()
web_7.save()
web_8.save()
web_9.save()
web_10.save()
web_10b_node.save()
web_10b_java.save()
web_11_node.save()
web_11_java.save()
web_12_node.save()
web_12_java.save()
web_13_node.save()
web_13_java.save()
web_13b_reconvene.save()
web_14.save()


#save ds
ds_1.save()
ds_2.save()
ds_3.save()
ds_4.save()
ds_5.save()
ds_6.save()
ds_7.save()
ds_8.save()
ds_9.save()
ds_10.save()
ds_11.save()
ds_12.save()
ds_13.save()
ds_14.save()
ds_15.save()
ds_16.save()
ds_17.save()
ds_18.save()
ds_19.save()
ds_20.save()
#save ux
ux_1.save()
ux_2.save()
ux_3.save()
ux_4.save()
ux_5.save()
ux_6.save()
ux_7.save()
ux_8.save()
ux_9.save()
ux_10.save()
ux_11.save()
ux_12.save()
ux_13.save()
ux_14.save()
ux_15.save()
ux_16.save()
ux_17.save()
ux_18.save()
ux_19.save()
ux_20.save()
#save ios
ios_1.save()
ios_2.save()
ios_3.save()
ios_4.save()
ios_5.save()
ios_6.save()
ios_7.save()
ios_8.save()
ios_9.save()
ios_10.save()
ios_11.save()
ios_12.save()
ios_13.save()
ios_14.save()
ios_15.save()
ios_16.save()
ios_17.save()
ios_18.save()
ios_19.save()
ios_20.save()

#save labs/careers/jobs
labs_1.save()
labs_2.save()
labs_3.save()
labs_4.save()

cs_1.save()
cs_2.save()
cs_3.save()
cs_4.save()

career_readiness_1.save()
career_readiness_2.save()
career_readiness_3.save()
career_readiness_4.save()
lambda_next.save()

job_yay.save()
ux_yay.save()

hired.save()
isa_payment.save()
vacation.save()
thankful.save()

# Link rooms together

# WEB TRACK -> North

orientation.connectRooms(web_1, "n")
web_1.connectRooms(orientation, "s")
web_1.connectRooms(web_2, "n")
web_2.connectRooms(web_1, "s")
web_2.connectRooms(web_3, "n")
web_3.connectRooms(web_2, "s")
web_3.connectRooms(web_4, "n")
web_4.connectRooms(web_3, "s")
web_4.connectRooms(web_5, "n")
web_5.connectRooms(web_4, "s")
web_5.connectRooms(web_6, "n")
web_6.connectRooms(web_5, "s")
web_6.connectRooms(web_7, "n")
web_7.connectRooms(web_6, "s")
web_7.connectRooms(web_8, "n")
web_8.connectRooms(web_7, "s")
web_8.connectRooms(web_9, "n")
web_8.connectRooms(web_7, "s")
web_9.connectRooms(web_10, "n")
web_9.connectRooms(web_8, "s")
web_10.connectRooms(web_9, "s")
##split off here
web_10.connectRooms(web_10b_node, "w")
web_10.connectRooms(web_10b_java, "e")
web_10b_node.connectRooms(web_10, "e")
web_10b_node.connectRooms(web_11_node, "n")
web_10b_java.connectRooms(web_10, "w")
web_10b_java.connectRooms(web_11_java, "n")
web_11_node.connectRooms(web_10b_node, "s")
web_11_node.connectRooms(web_12_node, "n")
web_11_java.connectRooms(web_10b_java, "s")
web_11_java.connectRooms(web_12_java, "n")
web_12_node.connectRooms(web_11_node, "s")
web_12_node.connectRooms(web_13_node, "n")
web_12_java.connectRooms(web_11_java, "s")
web_12_java.connectRooms(web_13_java, "n")
web_13_node.connectRooms(web_12_node, "s")
web_13_node.connectRooms(web_13b_reconvene, "e")
web_13_java.connectRooms(web_12_java, "s")
web_13_java.connectRooms(web_13b_reconvene, "w")
#intersect again
web_13b_reconvene.connectRooms(web_13_java, "e")
web_13b_reconvene.connectRooms(web_13_node, "w")
web_13b_reconvene.connectRooms(web_14, "n")
web_14.connectRooms(web_13b_reconvene, "s")
web_14.connectRooms(labs_1, "n")

# DS TRACK -> West

orientation.connectRooms(ds_1, "w")
ds_1.connectRooms(orientation, "e")

ds_1.connectRooms(ds_2, "w")
ds_2.connectRooms(ds_1, "e")

ds_2.connectRooms(ds_3, "n")
ds_3.connectRooms(ds_2, "s")

ds_3.connectRooms(ds_4, "n")
ds_4.connectRooms(ds_3, "s")

ds_4.connectRooms(ds_5, "n")
ds_5.connectRooms(ds_4, "s")

ds_5.connectRooms(ds_6, "n")
ds_6.connectRooms(ds_5, "s")

ds_6.connectRooms(ds_7, "n")
ds_7.connectRooms(ds_6, "s")

ds_7.connectRooms(ds_8, "n")
ds_8.connectRooms(ds_7, "s")

ds_8.connectRooms(ds_9, "n")
ds_9.connectRooms(ds_8, "s")

ds_9.connectRooms(ds_10, "n")
ds_10.connectRooms(ds_9, "s")

ds_10.connectRooms(ds_11, "n")
ds_11.connectRooms(ds_10, "s")

ds_11.connectRooms(ds_12, "w")
ds_12.connectRooms(ds_11, "e")

ds_12.connectRooms(ds_13, "n")
ds_13.connectRooms(ds_12, "s")

ds_13.connectRooms(ds_14, "n")
ds_14.connectRooms(ds_13, "s")

ds_14.connectRooms(ds_15, "n")
ds_15.connectRooms(ds_14, "s")

ds_15.connectRooms(ds_16, "n")
ds_16.connectRooms(ds_15, "s")

ds_16.connectRooms(ds_17, "n")
ds_17.connectRooms(ds_16, "s")

ds_17.connectRooms(ds_18, "n")
ds_18.connectRooms(ds_17, "s")

ds_18.connectRooms(ds_19, "n")
ds_19.connectRooms(ds_18, "s")

ds_19.connectRooms(ds_20, "e")
ds_20.connectRooms(ds_19, "w")
ds_20.connectRooms(labs_1, "e")



# UX -> South

orientation.connectRooms(ux_1, "s")
ux_1.connectRooms(orientation, "n")

ux_1.connectRooms(ux_2, 's')
ux_2.connectRooms(ux_1, 'n')

ux_2.connectRooms(ux_3, 's')
ux_3.connectRooms(ux_2, 'n')

ux_3.connectRooms(ux_4, 's')
ux_4.connectRooms(ux_3, 'n')

ux_4.connectRooms(ux_5, 's')
ux_5.connectRooms(ux_4, 'n')

ux_5.connectRooms(ux_6, 's')
ux_6.connectRooms(ux_5, 'n')

ux_6.connectRooms(ux_7, 's')
ux_7.connectRooms(ux_6, 'n')

ux_7.connectRooms(ux_8, 's')
ux_8.connectRooms(ux_7, 'n')

ux_8.connectRooms(ux_9, 's')
ux_9.connectRooms(ux_8, 'n')

ux_9.connectRooms(ux_10, 's')
ux_10.connectRooms(ux_9, 'n')

ux_10.connectRooms(ux_11, 's')
ux_11.connectRooms(ux_10, 'n')

ux_11.connectRooms(ux_12, 's')
ux_12.connectRooms(ux_11, 'n')

ux_12.connectRooms(ux_13, 's')
ux_13.connectRooms(ux_12, 'n')

ux_13.connectRooms(ux_14, 's')
ux_14.connectRooms(ux_13, 'n')

ux_14.connectRooms(ux_15, 's')
ux_15.connectRooms(ux_14, 'n')

ux_15.connectRooms(ux_16, 's')
ux_16.connectRooms(ux_15, 'n')

ux_16.connectRooms(ux_17, 's')
ux_17.connectRooms(ux_16, 'n')

ux_17.connectRooms(ux_18, 's')
ux_18.connectRooms(ux_17, 'n')

ux_18.connectRooms(ux_19, 's')
ux_19.connectRooms(ux_18, 'n')

ux_19.connectRooms(ux_20, 's')
ux_20.connectRooms(ux_19, 'n')

ux_20.connectRooms(ux_yay, 's')
ux_yay.connectRooms(ux_20, 'n')

# IOS -> East
orientation.connectRooms(ios_1, "e")
ios_1.connectRooms(orientation, "w")

ios_1.connectRooms(ios_2, 'e')
ios_2.connectRooms(ios_1, 'w')

ios_2.connectRooms(ios_3, 'n')
ios_3.connectRooms(ios_2, 's')

ios_3.connectRooms(ios_4, 'n')
ios_4.connectRooms(ios_3, 's')

ios_4.connectRooms(ios_5, 'n')
ios_5.connectRooms(ios_4, 's')

ios_5.connectRooms(ios_6, 'n')
ios_6.connectRooms(ios_5, 's')

ios_6.connectRooms(ios_7, 'n')
ios_7.connectRooms(ios_6, 's')

ios_7.connectRooms(ios_8, 'n')
ios_8.connectRooms(ios_7, 's')

ios_8.connectRooms(ios_9, 'n')
ios_9.connectRooms(ios_8, 's')

ios_9.connectRooms(ios_10, 'n')
ios_10.connectRooms(ios_9, 's')

ios_10.connectRooms(ios_11, 'n')
ios_11.connectRooms(ios_10, 's')

ios_11.connectRooms(ios_12, 'n')
ios_12.connectRooms(ios_11, 's')

ios_12.connectRooms(ios_13, 'n')
ios_13.connectRooms(ios_12, 's')

ios_13.connectRooms(ios_14, 'n')
ios_14.connectRooms(ios_13, 's')

ios_14.connectRooms(ios_15, 'n')
ios_15.connectRooms(ios_14, 's')

ios_15.connectRooms(ios_16, 'n')
ios_16.connectRooms(ios_15, 's')

ios_16.connectRooms(ios_17, 'n')
ios_17.connectRooms(ios_16, 's')

ios_17.connectRooms(ios_18, 'n')
ios_18.connectRooms(ios_17, 's')

ios_18.connectRooms(ios_19, 'n')
ios_19.connectRooms(ios_18, 's')

ios_19.connectRooms(ios_20, 'w')
ios_20.connectRooms(ios_19, 'e')
ios_20.connectRooms(labs_1, "w")

# Labs, etc...going north

labs_1.connectRooms(ios_20, "e")
labs_1.connectRooms(ds_20, "w")
labs_1.connectRooms(web_14, "s")
labs_1.connectRooms(labs_2, "n")
labs_2.connectRooms(labs_1, "s")
labs_2.connectRooms(labs_3, "n")
labs_3.connectRooms(labs_2, "s")
labs_3.connectRooms(labs_4, "n")
labs_4.connectRooms(labs_3, "s")
labs_4.connectRooms(cs_1, "n")

cs_1.connectRooms(labs_4, "s")
cs_1.connectRooms(cs_2, "n")
cs_2.connectRooms(cs_1, "s")
cs_2.connectRooms(cs_3, "n")
cs_3.connectRooms(cs_2, "s")
cs_3.connectRooms(cs_4, "n")
cs_4.connectRooms(cs_3, "s")
cs_4.connectRooms(career_readiness_1, "n")

career_readiness_1.connectRooms(cs_4, "s")
career_readiness_1.connectRooms(career_readiness_2, "n")
career_readiness_2.connectRooms(career_readiness_1, "s")
career_readiness_2.connectRooms(career_readiness_3, "n")
career_readiness_3.connectRooms(career_readiness_2, "s")
career_readiness_3.connectRooms(career_readiness_4, "n")
career_readiness_4.connectRooms(career_readiness_3, "s")
career_readiness_4.connectRooms(lambda_next, "n")

lambda_next.connectRooms(career_readiness_4, "s")
lambda_next.connectRooms(job_yay, "n")

job_yay.connectRooms(lambda_next, "s")

job_yay.connectRooms(hired, 'n')
hired.connectRooms(job_yay, "s")

hired.connectRooms(isa_payment, 'n')
isa_payment.connectRooms(hired, 's')

isa_payment.connectRooms(vacation, 'n')
vacation.connectRooms(isa_payment, 's')

vacation.connectRooms(thankful, 'n')
thankful.connectRooms(vacation, 's')


# r_foyer.connectRooms(r_overlook, "n")
# r_overlook.connectRooms(r_foyer, "s")

# r_foyer.connectRooms(r_narrow, "e")
# r_narrow.connectRooms(r_foyer, "w")

# r_narrow.connectRooms(r_treasure, "n")
# r_treasure.connectRooms(r_narrow, "s")

players=Player.objects.all()
for p in players:
  p.currentRoom=orientation.id
  p.save()

