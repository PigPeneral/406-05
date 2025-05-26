<?php
    $name= $_POST["name"];
    $context= $_POST["context"];
?>

<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>您的回覆</title>
</head>
<body>
    <h1>感謝您的回覆</h1>
    <fieldset>
        <legend>確認您的回覆內容</legend>
        <p>姓名: <?php echo htmlspecialchars($name); ?></p>
        <p>內容: <?php echo nl2br(htmlspecialchars($context)); ?></p>
        <a href="exerciser-0523.test.html">返回首頁</a>
    </fieldset>
</body>
</html>