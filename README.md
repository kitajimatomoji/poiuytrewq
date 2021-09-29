# Utility
ユーティリティークラス

機能を提供するユーティリティー。
主に。


# 使い方

## log
ログを出力します。
```
Utility::log($SPIRAL, __FILE__, __LINE__, $param_list);
Utility::log($SPIRAL, __FILE__, __LINE__, $some_flag);
```

出力した情報は、 *print* で表示できます。

## print
下記コード、 *log* で出力したログを表示できます。
「ページのソースを表示」モードで表示しましょう。
**誰でも参照できる状態にならないよう、配慮をお願いします。**

    <!--sample-->
    <?php
    require('Utility.class.php');
    Utility::print($logger);
    ?>

## callApi


# Install
![Step1](sample.PNG)
画像を組み込みます。
* ソースフォルダ：（空白）
* 名前：Utility.class

