from dataclasses import dataclass
from plyer import notification 
import numpy  as np #numpy with np as alias
import matplotlib.pyplot as plt #for plotting graphs
import time
import schedule

#Notification functions
def notifyMe(title, message):
    notification.notify(
    title = title,
    message = message,
    app_icon = "icon.ico",
    timeout = 10,
    )

def notifyMe1():
    notification.notify(
    title = "Congratulations!!",
    message = "You have completed today's goal",
    app_icon = "icon.ico",
    timeout = 10,
    )
    
#Start
print("\t\t\t  Welcome to Calorie tracker\n\t\tMonitor your fitness..by counting your calories \n")

#Taking calorie goals from user 
calories_goal_limit=int(input("Enter the total Calories you aim to consume "))
protein_goal=int(input("Enter the grams of Proteins you aim to consume "))
fat_goal=int(input("Enter the grams of Fats you aim to consume "))
carbs_goal=int(input("Enter the grams of Carbohydrates you aim to consume "))
today=[]#List of food consumed 
@dataclass
class Food:
    name:str
    calories:int
    protein:int
    fat:int
    carbs:int
done=False
while not done:
    print("\n(1) Add new food\n(2) Visualize progress\n(3) Quit")
    choice=input("Choose an option")
    if choice =="1":
        print("Enter food details")
        name=input("Name:")
        calories=int(input("Calories:"))
        protein=int(input("Proteins:"))
        fat=int(input("Fats:"))
        carbs=int(input("Carbohydrates:"))
        food=Food(name,calories,protein,fat,carbs)
        today.append(food)
        print(name,"is added")

        calories_sum=sum(food.calories for food in today)
        protein_sum=sum(food.protein for food in today)
        fat_sum=sum(food.fat for food in today)
        carbs_sum=sum(food.carbs for food in today)
        
#Calling notification function
        if __name__ == '__main__':
            left=str(calories_goal_limit-calories_sum)
            notifyMe("Calories left to reach goal:",left)
        
    elif choice =="2":
        
        fig, axs=plt.subplots(2,2)
        
        #Pie chart of distribution of nutrients
        axs[0,0].pie([protein_sum,fat_sum,carbs_sum],labels=["Proteins","Fats","Carbohydrates"],autopct="%1.1f%%")
        axs[0,0].set_title("Distribution of nutrients consumed")
        
        #Bar Graph of Nutrients intake VS Goal 
        axs[0,1].bar(["Protein\ntaken","Fat\ntaken","Carbs\ntaken"],[protein_sum,fat_sum,carbs_sum],width=0.4)
        axs[0,1].bar(["Protein\ngoal","Fat\ngoal","Carbs\nGoal"],[protein_goal,fat_goal,carbs_goal],width=0.4)
        axs[0,1].set_title("Progress in nutrients")
        

        #Pie chart of Nutrients intake VS Goal 
        axs[1,0].pie([calories_sum,calories_goal_limit-calories_sum],labels=["Calories consumed","Remaining Calories"],autopct="%1.1f%%")
        axs[1,0].set_title("Calories Goal Progress")
        
        #Line graph showing progress in Calorie consumption through different food items
        axs[1,1].plot(list(range(len(today))),np.cumsum([food.calories for food in today]),label="Calories consumed")
        axs[1,1].plot(list(range(len(today))),[calories_goal_limit]*len(today),label="Calorie Goal")
        axs[1,1].legend()
        axs[1,1].set_title("Calories Goal Progress")
        
        fig.tight_layout()
        plt.show()
    elif choice =="3":
        print("THANK YOU!!\nSTAY HEALTHY AND HAPPY!!")
        done=True
    else:
        print("Invalid Choice!")
        
#Notification         
def notifyMe2():
    notification.notify(
    title ="Calories left in for completing today's Goal:",
    message = left,
    app_icon = "icon.ico",
    timeout = 10,
    )

#Show Visualizer at the end of the day
def show_last():
    plt.pie([calories_sum,calories_goal_limit-calories_sum],labels=["Calories consumed","Remaining Calories"],autopct="%1.1f%%")
    plt.show()

#Schedule the notification and visualizer        
if calories_goal_limit-calories_sum==0:
    schedule.every().day.at("11:30").do(notifyMe1)
    schedule.every().day.at("11:30").do(show_last)
    while True:
        schedule.run_pending()
        time.sleep(1)
        
else:
    schedule.every().day.at("11:30").do(notifyMe2)
    schedule.every().day.at("11:30").do(show_last)
    while True:
        schedule.run_pending()
        time.sleep(1)
        
