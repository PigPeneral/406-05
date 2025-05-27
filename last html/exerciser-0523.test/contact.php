<?php
    $name= $_POST["name"];
    $context= $_POST["context"];
?>

<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="refresh" content="5; url=exerciser-0523.test.html">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=LXGW+WenKai+TC&display=swap" rel="stylesheet">
    <title>您的回覆</title>
    <style>
        body {
            font-family: 'LXGW WenKai TC', sans-serif;
            color: rgb(50, 50, 50);
            background: #EBDAE3;
            background: linear-gradient(90deg, rgba(235, 218, 227, 1) 0%, rgba(122, 29, 253, 0.45) 50%, rgba(252, 69, 197, 0.58) 100%);
            text-align: center;
        }
        fieldset {
            background-color: rgb(253, 230, 255);
            font-size: large;
            width: 50%; 
            margin: auto;
            padding: 20px;
            border-radius: 10px;
        }
    </style>
</head>
<body>
    <h1>感謝您的回覆</h1>
    <fieldset>
        <legend>您的回覆內容</legend>
        <p>姓名: <?php echo htmlspecialchars($name); ?></p>
        <p>內容: <?php echo nl2br(htmlspecialchars($context)); ?></p>
        <a href="exerciser-0523.test.html">返回首頁</a>
    </fieldset>
</body>
</html>