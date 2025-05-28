<?php
// login.php
$username = $_POST["username"];
$password = $_POST["password"];
?>

<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>登入中</title>
    <style>
        body {
            font-family: 'LXGW WenKai TC', sans-serif;
            color: rgb(50, 50, 50);
            background: #EBDAE3;
            background: linear-gradient(90deg, rgba(235, 218, 227, 1) 0%, rgba(122, 29, 253, 0.45) 50%, rgba(252, 69, 197, 0.58) 100%);
            text-align: center;
            animation: gradient 15s ease infinite;
        }
        #mes {
            background-color: rgb(253, 230, 255);
            font-size: large;
            width: 50%;
            margin: auto;
            padding: 20px;
            border-radius: 10px;
        }
        @keyframes  gradient {
            0% {
                background-position: 0% 15%;
            }
            50% {
                background-position: 50% 15%;
            }
            100% {
                background-position: 0% 15%;
            }
        }
    </style>
</head>
<body>
    <div id="mes" style="margin: auto;">
        <?php
        if ($username === "admin" && $password === "0000") {
            echo "<h1>歡迎，$username ！</h1>";
        } elseif ($username === "Guest" && $password === "1234") {
            echo "<h1>歡迎，$username ！</h1>";
        } else {
            echo "<h1>登入失敗，請檢查您的帳號或密碼。</h1>";
        }
        ?>
        網頁跳轉中，請稍後...
        <script>
            setTimeout(function() {
                window.location.href = "/exerciser-0523.html";
            }, 10000); // 10秒後跳轉
        </script>
        <p>如果沒有自動跳轉，請點擊<a href="/exerciser-0523.html">這裡</a>。</p>
        </div>
</body>
</html>