# asobi

<h2>〜TCP編〜</h2>  

ソケット通信でTurtleBotの遠隔操作  

クライアント側にclient.pyを持ってちゃってください。  
サーバー側はmove.pyを使います。  
server.pyはソケット通信のみのファイルです。  

使い方は簡単！！  

１．ROSとTurtleBotの環境整えま〜す  

２．ワークスペース内にこのディレクトリをクローンしま〜す  

３．サーバー側で「sudo apt install net-tools」やってない人はやってくださ〜い  

４．サーバー側で「ifconfig」で自分のIPアドレスみま〜す  

５．そのIPアドレスをbindしちゃってくださ〜い  

６．クライアント側をサーバ側と同じネットワークに接続しま〜す  

７．クライアント側の接続先もサーバーのIPアドレスにしちゃってくださ〜い  

８．はい、じゃあ、「roslaunch turtlebot_bringup minimal.launch」でTurtleBot立ち上げて〜  

９.「./move.py」でサーバー立ち上げて〜  

１０．「python3 client.py」でもなんでもいいからクライアント立ち上げて〜  

１１．クライアント側で0か1を入力しちゃいましょう！！0は進めで1は戻れで〜す！！  

１２．なんということでしょ〜う！！TurtleBotが動いているではありませんか！！  
  
<hr>
<h2>〜UDP編〜</h2>  
 
使い方は基本TCPとあんま変わんないんで省略しながら説明しま〜す  

今回は下の画像のコントローラー使ってま〜す  
https://www.sony.com/articleimage/servlet/servlet.FileDownload?file=0155F000007WwGaQAK  

はい、タートルボットをいい感じにしたサーバー側でmove.py立ち上げて〜  

クライアント側でコントローラーと接続して、joystick_client.py立ち上げて〜  

コントローラーの真ん中のボタンをポチッと押すと情報が流れ始めま〜す！  

そう！これがラジコンならぬUDPコン！！(嘘です)  
