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


function CreateCategory() {
    const csrf = document.getElementById("csrf_token").value;

    document.getElementById("CategoryDiv").innerHTML =
    `<form method="POST">
        <input type="hidden" name="csrfmiddlewaretoken" value="${csrf}">
        <input type="text" name="CatName" placeholder="Category Name" required><br><br>
        <input type="text" name="CatDes"  placeholder="Description" required><br><br>
        <button type="submit" class="save-category-btn">Save Category</button>
     </form>`;
}

