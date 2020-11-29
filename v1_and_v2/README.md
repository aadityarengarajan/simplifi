<h1>Simplifi</h1>
Task Manager for automatically creating daily tasklists.
<h1>How to use</h1>
Edit .XLSX file to edit task list.<br><br>
    <b><i>!! Do NOT change column names, or the name of the XLSX file !!</b></i><br>
    <b>JOB</b> column gets a brief/summarized job name.<br>
    <b>JOB DESCRIPTION</b> column should have the complete details of the job.<br>
    <b>DEADLINE</b> column should have the deadline for the job in the format MM/DD/YY.<br>
    <b>DAYS NEEDED</b> column should have the estimated number of days required to complete the task.<br>
    <b>CATEGORY</b> column can have a name for the category/type of job.<br>
    <b>COMPLETION</b> column should be blank if job is incomplete, have anything typed in it (example, an 'X') if the job is complete.<br>
    <b>PRIORITY</b> column should have a number to describe the priority of the job in the sense :<br>
                    - '3' for normal jobs.<br>
                    - '2' for urgent jobs.<br>
                    - '1' for emergency jobs.<br>
    <b>TODAY</b> column will be automatically updated with the current date using the excel formula '=TODAY()' which has to be input by the user for every new job created.<br>
    <b>DAYS LEFT</b> column will also be automatically updated with the # of days left to reach deadline by using practical formula today - deadline, excel formula '=C2-H2' which has to be input by the user for every new job created.<br><br>

Once done filling XLSX, run 'Simplifi.py' to geneate a dashboard consisting of :
  - A report of total # of jobs<br>
  - A report of incomplete jobs<br>
  - A report of complete jobs<br>
  - A graph of the reported data<br>
  - A calendar with deadlines marked automatically<br>
  - A list of tasks to perform <b>today</b> created automatically based on the given tasks and their deadlines! :-)<br>
  
The dashboard will have different wallpapers based on the time of the day (morning, evening, night) :-)
<h2><i>REQUIRES PANDAS MODULE</i></h2>


<h1>Simplifi v2 : Changelog</h1>
The second version provides you with a customized newspaper everyday, with personalized topics straight from Google News!<br>
Do remember to change the news topics of interest, the current topics are my personal topics of interest and you may not be interested in the same.
<h2><i>REQUIRES PANDAS AND GOOGLENEWS MODULE</i></h2>
