# Docuworks Assessment

This is a general program that, through usage of the command line, can read and edit .txt files.
This includes being able to display the given text, but also search and replace words and find email-addresses within the document

# Used third-party packages
* Click : a command-line interface library

# Current Functions

* --load : loads the base file into a temporary file, allowing changes without changing the base file.
* --display : displays the text from the temporary file, so the file after all the changes youve made since last loading the file
* --search : searches through the document for a given word and returns the start and end location of any usages of said word
* --replace: searches through the document and replaces one word with another, based on the input
* --wordfrequency: calculates the most used words in a file and returns both the word and how many usages it had.
  It is possible to change the amount of words you want to see.
* --palindromes : runs through every word within a document and returns every palindrome it can find
* --emailsearch : runs through the document and returns any valid emailaddress it can find
* --decoder : searches for misplaced capitalized letters and runs it through a Ceasars cypher, based what you input as its shift
* --save : Saves the appended file to the base file, saving any changes made during the progress of editing the file
* --reset : Returns the appended file back to the base file, resetting any changes made.

# Usage
The way to currently use the program is to input:
* python "main/file/location.py" "target/file/location.txt" --load 1                  
  Now you have loaded the file and created an temp file in which u can make changes
* python "main/file/location.py" "target/file/location.txt" --[function] 1          
  Replace --[function] with the above mentioned functions to do what u want the program to do
* python "main/file/location.py" "target/file/location.txt" --save 1            
  This saves the temp file to the base file, saving it                        
  (only do this when u are sure its how u want it to be, use --display to see how it would look)

# Missing components
* Streamlining Click commands:
  > this includes issues like every function needing atleast some argument to work. This is something I dont want, but didnt have the time to find out how to change
* Unittesting:
  > mainly missing because of time constraints, however I have also not used Unittest a lot, so it would have probably taken quite a bit of time to create an acceptable test
* Comments:
  > I should have written more comments during the programming. I personally believe the code is decently readable, but its possible that someone else would beg to differ

# Issues I ran into during the project
* Time management
  > Instead of using 7+ hours understanding Click, I should have continued with the other parts of the project
* Planning
  > Instead of doing everything in order, I should have done the parts I was unfamiliar first, so I could have asked questions Wednesday/Thursday
* Be more diligent with reading documentation
  > One of the Issues I ran into with Click is that I fundamentally misunderstood how the package worked, leading to behaviour that took way too long to fix. Instead I should have spend more time focussing on diligently reading through the base parts of the documentation
* Read the Assignment more carefully
  > I only recently saw the part in the DoD about frequent changes and logs in Git. This should not happen in a work environment.


 
  


