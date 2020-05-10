import os

class html_writer():

	def __init__(self):
		self.website_name = 'My Shoping center'
		self.website_tagline = 'This is my tagline'
		self.button_title='Buy now'

		self.navbar_font_color = 'navbar-dark'
		self.dropdown_font_color = 'text-light'
		self.footer_font_color='text-warning'
		
		self.body_bgcolor = 'bg-light'
		self.navbar_bgcolor = 'bg-dark'
		self.dropdown_bgcolor = 'bg-dark'
		self.card_bgcolor='bg-dark'
		self.footer_bgcolor='bg-dark'
		self.button_color='bg-warning'

		self.card_font_size='h2'
		self.footer_font_size='h2'
		self.card_title_align='float-left'
		self.button_align='float-right'
		self.footer_font_align='text-center'

	def navbar_wrtier(self):
		nav_html = """
		<section class="sticky-top">
			<nav class="navbar """+self.navbar_font_color+" "+self.navbar_bgcolor+""" text-right ">
				
				<button class="navbar-toggler btn" data-toggle="collapse" data-target="#TheNavbar"><span class="h2 text-warning">&#x2630;</span></button>
				<section class="navbar-brand">					
					<section class="navbar-text mr-5 p-2 bg-warning rounded text-dark ">Hello user</section>
                    <span class="font-weight-bold text-left" style="font-size: 35px">"""+self.website_name+"""</span>
                    <br>
					<small>"""+self.website_tagline+"""</small> 
				</section>
            </nav>           
			<section class="collapse bg-danger" id="TheNavbar">
				<ul class="list-group border-0 list-group-flush ">
					<li class="list-group-item """+self.dropdown_bgcolor+""" "><a href="#" class="h3 """+self.dropdown_font_color+""" " style="text-decoration: none;"><section>Home</section></a></li>
					<li class="list-group-item """+self.dropdown_bgcolor+""" "><a href="#" class="h3 """+self.dropdown_font_color+""" " style="text-decoration: none;"><section>Register</section></a></li>
					<li class="list-group-item """+self.dropdown_bgcolor+""" "><a href="#" class="h3 """+self.dropdown_font_color+""" " style="text-decoration: none;"><section>Login</section></a></li>
					<li class="list-group-item """+self.dropdown_bgcolor+""" "><a href="#" class="h3 """+self.dropdown_font_color+""" " style="text-decoration: none;"><section>About</section></a></li>
				</ul>
			</section>
		</section>
		"""
		return nav_html

	def carousel_writer(self):
		slide_show = """
		<section class="row mt-3"><!-- The Slide show -->		
			<section class="col-sm-12 ">
				<section class="carousel slide carousel-fade text-center mx-auto" id="TheMovingImages" data-ride="carousel">
					<ol class="carousel-indicators text-center w-25 rounded mx-auto">
						<li data-target="#TheMovingImages" data-slide-to="0" class="active"></li>
						<li data-target="#TheMovingImages" data-slide-to="1"></li>
						<li data-target="#TheMovingImages" data-slide-to="2" ></li>
						<li data-target="#TheMovingImages" data-slide-to="3"></li>
					</ol>
					<section class="carousel-inner">
						<section class="carousel-item"><img src="images/slide_img1.jpg"  class="rounded"  height="600px" width="1600px"></section>
						<section class="carousel-item"><img src="images/slide_img2.jpg"  class="rounded" height="600px" width="1600px"></section>
						<section class="carousel-item "><img src="images/slide_img3.jpg"  class="rounded" height="600px" width="1500px"></section>
						<section class="carousel-item active"><img src="images/slide_img4.jpg" class="rounded"  height="600px" width="1600px"></section>
					</section>
				</section>
			</section>
		</section>
		"""
		return slide_show

	def card_writer(self):
		card_html = """
		<section class="row mt-5">

			<section class="col-md-4">
				<section class="card text-warning """+self.card_bgcolor+""" rounded ml-2 mr-2 p-4">
					<img src="images/iphone.png" class="card-img-top" height="530px">
					<section class="card-body" style="display: inline-block;">
						<section class=" """+self.card_font_size+""" font-weight-bold """+self.card_title_align+"""">IPhone 5S</section>
						<button class="btn rounder """+self.button_color+""" text-dark h3 """+self.button_align+""" ">"""+self.button_title+"""</button>
					</section>
				</section>
			</section>

			<section class="col-md-4">
				<section class="card text-warning """+self.card_bgcolor+""" rounded ml-2 mr-2 p-4">
					<img src="images/cloth.png" class="card-img-top" height="530px">
					<section class="card-body" style="display: inline-block;">
						<section class=" """+self.card_font_size+""" font-weight-bold """+self.card_title_align+"""">Formal mens suit</section>
						<button class="btn rounder """+self.button_color+""" text-dark h3 """+self.button_align+""" ">"""+self.button_title+"""</button>
					</section>
				</section>
			</section>

			<section class="col-md-4">
				<section class="card text-warning """+self.card_bgcolor+""" rounded ml-2 mr-2 p-4">
					<img src="images/headphones.png" class="card-img-top" height="530px">
					<section class="card-body" style="display: inline-block;">
						<section class=" """+self.card_font_size+""" font-weight-bold """+self.card_title_align+"""">Wireless Headphone</section>
						<button class="btn rounder """+self.button_color+""" text-dark h3 """+self.button_align+""" ">"""+self.button_title+"""</button>
					</section>
				</section>
			</section>
		
			</section>
		"""
		return card_html

	def footer_writer(self):
		footer_writer = """
		<br><br><br><br><br><br><br><br><br>
		<section class=" """+self.footer_bgcolor+' '+self.footer_font_color+' ' +self.footer_font_size+' '+self.footer_font_align+""" border">
			"""+self.website_name+"""<br>
			<h3>Copyright 2008-2015   All rights reserved. Powered By BigMarket Platform</h3>
		</section>
		"""
		return footer_writer

	def header_writer(self):
		start_html = """
    	<!DOCTYPE html>
    	<html>
    		<head>
    			<meta charset="utf-8">
    			<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no user-scalable=no">
    			<link rel="stylesheet" href="../libs/bootstrap.min.css">
    			<title>"""+self.website_name+"""</title>
            	<script src="../libs/jquery-3.4.1.slim.min.js"></script>
		    	<script src="../libs/popper.min.js"></script>
		    	<script src="../libs/bootstrap.min.js"></script>
    		</head>
			<body class=" """+self.body_bgcolor+""" ">"""+self.navbar_wrtier()+" "+self.carousel_writer()+" "+self.card_writer()+" "+self.footer_writer()+"""</body></html>"""
		return start_html

	def file_writer(self):

		f = open(os.path.abspath("html_pages/index.html"),"w")
		head_tag = self.header_writer()
		f.write(head_tag)
		f.close()

obj = html_writer()
obj.file_writer()
