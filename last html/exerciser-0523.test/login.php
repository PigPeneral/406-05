<?php
// login.php
$username = $_POST["username"];
$password = $_POST["password"];
if ($username === "admin" && $password === "0000") {
    echo "<h1>歡迎，$username ！</h1>";
} elseif ($username === "Guest" && $password === "1234") {
    echo "<h1>歡迎，$username ！</h1>";
} else {
    echo "<h1>登入失敗，請檢查您的帳號或密碼。</h1>";
}
?>

<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>登入中</title>
</head>
<body>
    <div id="mes" style="margin: auto;">
    網頁跳轉中，請稍後...
    <script>
        setTimeout(function() {
            window.location.href = "index.php";
        }, 10000); // 10秒後跳轉
    </script>
    <p>如果沒有自動跳轉，請點擊<a href="index.php">這裡</a>。</p>
    </div>
</body>
</html>