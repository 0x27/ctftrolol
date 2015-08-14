<?php
	$login=@$_POST['login'];
	$password=@$_POST['password'];
    if(@$login=="admin" && sha1(@$password)==$pwhash){
    	include 'secretdir/flag';
    }else{
?>
	<center>
		login<br/><br/>
		<form action="" method="POST">
			<input name="login" placeholder="login"><br/>
			<input name="password" placeholder="password"><br/><br/>
			<input type="submit" value="Go!">
		</form>
	</center>
<?php
    }
?>
