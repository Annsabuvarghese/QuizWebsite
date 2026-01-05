function create() {
    document.getElementById("QuestionBox").innerHTML =

        "<input type='text' name='question' class='inputBox' placeholder='Enter the question' required><br><br>" +
       
        "<input type='radio' name='CorrectAns' value='op1' required>" +
        "<input type='text' name='op1' class='inputBox' placeholder='Enter the option1' required><br><br>" +



        "<input type='radio' name='CorrectAns' value='op2' required>" +
        "<input type='text' name='op2' class='inputBox' placeholder='Enter the option2' required><br><br>" +



        "<input type='radio' name='CorrectAns' value='op3' required>" +
        "<input type='text' name='op3' class='inputBox' placeholder='Enter the option3' required><br><br>" +


        "<input type='radio' name='CorrectAns' value='op4' required>" +
        "<input type='text' name='op4' class='inputBox' placeholder='Enter the option4' required><br>" 

}


// CreateCategory()
function CreateCategory() {
    document.getElementById("CategoryDiv").innerHTML =
    "<input type='text' name='CatName' class='CatBox' placeholder='Enter the Category name here' required><br><br>" +
    "<input type='text' name='CatDes' class='CatBox' placeholder='Enter the Category description here' required><br><br>" +
    "<button type='submit'>Create Cat</button>";

}
