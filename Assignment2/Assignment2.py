#Abdulkadir Parlak 2210765025
import os

current_dir_path = os.getcwd()#To make the program runnable for every operating system.
readingFileName = "doctors_aid_inputs.txt"
readingFilePath = os.path.join(current_dir_path, readingFileName)

writingFileName = "doctors_aid_outputs.txt"
writingFilePath = os.path.join(current_dir_path, writingFileName)

def read_inputs():
    result = ""
    with open(readingFilePath, "r", encoding="utf-8") as inputFile:
        for line in inputFile:
            if line.startswith("create"):
                line = line[7:-1]
                lineList = line.split(",")
                patientName = lineList[0]#Here I am defining the create function's arguments as taking inputs from a txt file.
                diagnosisAccuracy = float(lineList[1])
                diseaseName = lineList[2]
                diseaseIncidence = lineList[3]
                exceptionList = diseaseIncidence.split("/")#Here I struggled to convert string to float. So I did such a thing.
                temp_DI = float(int(exceptionList[0])/int(exceptionList[1]))
                treatmentName = lineList[4]
                treatmentRisk = float(lineList[5])
                result += create(patientName, diagnosisAccuracy, diseaseName, diseaseIncidence, treatmentName, treatmentRisk)
            elif line.startswith("remove"):
                if "\n" in line:#I realized an error so I edited it but after report. So, the report doesn't include this parts.
                    line = line[7:-1]
                else:
                    line = line[7:]
                patientName = line
                result += remove(patientName)
            elif line.startswith("list"):
                result += List()
            elif line.startswith("recommendation"):
                if "\n" in line:
                    line = line[15:-1]
                else:
                    line = line[15:]
                patientName = line
                result += recommendation(patientName)
            elif line.startswith("probability"):
                if "\n" in line:
                    line = line[12:-1]
                else:
                    line = line[12:]
                patientName = line
                result += str(probability(patientName))
    return result#I merged all the outputs which is produced by the functions together and at the end returned it.

def write_outputs():#This functions writes the outputs, which is taken from a txt file, to another txt file.
    with open(writingFilePath, "w", encoding="utf-8") as outputFile:
        outputFile.write(read_inputs())#read_inputs() returns the all output in one go. It returns a string value.

def create(patientName, diagnosisAccuracy, diseaseName, diseaseIncidence, treatmentName, treatmentRisk):
    PatientDataList = [patientName, diagnosisAccuracy, diseaseName, diseaseIncidence, treatmentName, treatmentRisk]
    for i in PatientNameList:
        if i == patientName:
            return "Patient {} cannot be recorded due to duplication.\n".format(patientName)
    InformationList.append(PatientDataList)
    PatientNameList.append(patientName)
    return "Patient {} is recorded.\n".format(patientName)

def remove(patientName):
    for i in range(len(PatientNameList)):
        if patientName == PatientNameList[i]:
            InformationList.remove(InformationList[i])
            PatientNameList.remove(patientName)
            return "Patient {} is removed.\n".format(patientName)
    return "Patient {} cannot be removed due to absence.\n".format(patientName)

def List():
    result = "Patient Diagnosis   Disease         Disease      Treatment       Traeatment\n"#Creating the headers of the table.
    result +="Name    Accuracy    Name            Incidence    Name            Risk\n"
    result +="---------------------------------------------------------------------------\n"
    sub_result = ""#sub_result holds the result of the printing out of the InformationList. I am adding it to the variable "result" to merge headers and the values of the table.
    i = 0
    while (i < len(InformationList)):
        a = InformationList[i]
        sub_result += a[0]
        sub_result += " " * (8 - len(a[0]))
        sub_result += "{:.2%}".format(a[1])
        sub_result += " " * 5
        sub_result += a[2]
        sub_result += " " * (16 - len(a[2]))
        sub_result += a[3]
        sub_result += " " * 3
        sub_result += a[4]
        sub_result += " " * (17 - len(a[4]))
        sub_result += "{:.0%}".format(a[5])
        sub_result += "\n"
        i += 1
    result += sub_result#The variable "result" has the final output of the "List()" function.
    return result

def recommendation(patientName):
    for i in range(len(PatientNameList)):
        if PatientNameList[i] == patientName:
            diseaseIncidence = InformationList[i][3]# I know I repeated myself a lot and I shouldn't have done it but I couldn't manage how to use the probability value that I calculated inside the probability function.
            exceptionList = diseaseIncidence.split("/")#Here I am pulling the values which I will use, from the list called InformationList.
            temp_DI = float(int(exceptionList[0]) / int(exceptionList[1]))
            diagnosisAccuracy = InformationList[i][1]
            result = temp_DI * (diagnosisAccuracy / (1 - diagnosisAccuracy))
            diagnosisAccuracy = InformationList[i][1]
            treatmentRisk = InformationList[i][5]
            result = temp_DI * (diagnosisAccuracy / (1 - diagnosisAccuracy))
            pb = round(((result/(result+1))*100),2)
            if pb > (treatmentRisk)*100:
                return "System suggests {} to have the treatment.\n".format(patientName)
            else:
                return "System suggests {} NOT to have the treatment.\n".format(patientName)
    return "Recommendation for {} cannot be calculated due to absence.\n".format(patientName)

def probability(patientName):
    for i in range(len(PatientNameList)):
        if PatientNameList[i] == patientName:
            diseaseName = InformationList[i][2]#Here I am pulling the values which I will use, from the list called InformationList.
            diseaseIncidence = InformationList[i][3]
            exceptionList = diseaseIncidence.split("/")
            temp_DI = float(int(exceptionList[0]) / int(exceptionList[1]))
            diagnosisAccuracy = InformationList[i][1]
            result = temp_DI*(diagnosisAccuracy/(1-diagnosisAccuracy))
            pb = round(((result/(result+1))*100),2)
            if pb%10 == 0:
                pb = int(pb)
            return "Patient {} has a probability of {}% of having{}.\n".format(patientName,pb,diseaseName.lower())
    return "Probability for {} cannot be calculated due to absence.\n".format(patientName)

InformationList = []#This list contains all the information about patients. It is a 2-Dimensional list.
PatientNameList = []#In order to check the patients' existence, I created a list which contains the names of the patients.

write_outputs()#The whole program works with just 1 simple call.