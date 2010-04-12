<html>
<head>
    <title>Little iBird</title>
    <meta name="viewport" content="user-scalable=no, width=device-width" />
    <link rel="stylesheet" type="text/css" href="/static/iphone.css" media="only screen and (max-width: 480px)" />
    <link rel="stylesheet" type="text/css" href="/static/desktop.css" media="screen and (min-width: 481px)" />
    <!--[if IE]> 
    <link rel="stylesheet" type="text/css" href="../media/css/explorer.css" media="all" /> 
    <![endif]-->
    <script type="text/javascript" src="/static/jquery.js"></script>
    <script type="text/javascript" src="/static/iphone.js"></script>  
</head>

<body>
<div id="container">
            <div id="header">
                <h2>{{title}}</h2>
                <div id="utility">
                    <ul>
                        <li><a href="http://blog.digvan.com/?page_id=2">About</a></li>
                        <li><a href="http://blog.digvan.com/">Blog</a></li>
                    </ul>
                </div>
            </div>
  <div id="content">
	%if name:
		<p> Your name is: <b>{{ name }}</b> </p>
		<p> Your followers count is: <b>{{ user.followers_count }}</b> </p>
		<p> Your friends count is: <b>{{ user.friends_count }}</b> </p>
	<p> Your latest status is: <b>{{ user.status.text }}</b> </p>
	%else:
		<p>Please click on below link to sign in</p> 
		<a href="/twitter/signin" ><img alt="connect to twitter" src="/static/tc.png"/></a>
	%end
	</div>
<div id="footer">
    <p> Powered by Redis and Bottle </p>
	<p> Design by: Khashayar Dehdashtinejad </p>
</div>
</div>
</body>
</html>
