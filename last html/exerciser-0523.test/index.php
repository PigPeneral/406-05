<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>首頁</title>
    <style>
        nav.toptext{
            display: flex;
            justify-content: left;
            align-items: center;
            letter-spacing: 1px;
            background-color: #e0f1f0;
            padding: 20px;
            margin-bottom: 10px;
            gap: 20px;
            box-shadow: 8px 8px 12px -6px rgba(0, 0, 0, 0.1);
        }
        nav.sidetext {
            display: inline-flex;
            flex-direction: row;
            width: 104px;
            align-items: left;
            background-color: #e0f1f0;
            padding: 20px 20px 20px 0;
            box-shadow: 5px 5px 10px -6px rgba(0, 0, 0, 0.1);
        }
        div.main {
            display: inline-flex;
            width: 60vw;
            height: 100vh;
        }
    </style>
</head>
<body style="background-color: rgb(235, 218, 227);">
    <!--nav-->
    <nav class="toptext">
        <img src="/img/ROC_Workforce_Development_Agency_Emblem.png" alt="LOGO" width="200" height="200">
        <a href="exerciser-0523.test.html" title="首頁">首頁</a>
        <a href="bio.html" title="自我介紹">自我介紹</a>
        <a href="contact.html" title="聯絡我">聯絡我</a>
    </nav>
    <hr>
    <!--side-->
    <aside>
        <nav class="sidetext">
            <ul>
                <li><a href="exerciser-0523.test.html" title="首頁">首頁</a> </li>
                <li><a href="bio.html" title="自我介紹">自我介紹</a> </li>
                <li><a href="contact.html" title="聯絡我">聯絡我</a> </li>
            </ul>
        </nav>
    </aside>
    <!--end of side; content-->
    <!--main-->
    <main>
        <div class="main">
            <span>
                <h1>Index！</h1>
                <p>Lorem!</p>
                <p>假文!</p>
            </span>
        </div>
    </main>
</body>
</html>