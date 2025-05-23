<?php
    $username = $_POST["username"];
    $usersex = $_POST["usersex"];
    $edu_lev = $_POST["edu_lev"];
    $UserAbilities = $_POST['UserAbilities'];
    $Detail = $_POST["Detail"];
?>

<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>結果</title>
    <style>
        .lightpink {
            background-color: lightpink;
            font-size: large;
            text-align: center;
            color: black;
        }
        .green {
            background-color: green;
            font-size: large;
            text-align: center;
            color: bisque;
        }
        table {
            width: 30%;
            margin: auto;
            border: 1px solid black;
            border-collapse: collapse;
        }
    </style>
</head>
<body>
<?php
    if($usersex == "male"){
        echo "<div class='lightpink'>";
        echo "<h1>$username 先生的資訊</h1>";
    }else{
        echo "<div class='green'>";
        echo "<h1>$username 小姐的資訊</h1>";
    }

    echo "學歷:" . $edu_lev . "<br>";
    echo "<table class=table>";
        echo "<tr><th>能力:</th></tr>";
        foreach($_POST['UserAbilities'] as $ability){
            echo "<tr><td><ol>" . $ability . "</ol></td></tr>";
        }
    echo "</table>";

    echo "您的能力細節:<br>";
    echo "<p>" . $Detail . "</p>";
?>
<a href="/try.html" title="back to try.html" style="font-size:x-large;">retry</a>
</div>
</body>
</html>