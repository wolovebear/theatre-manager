from theatre_manager import app
from flask import Flask, render_template, request, session
import mysql.connector

@app.route('/listmovies')
def listMovies():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = (
        "SELECT * FROM Movie ORDER BY MovieName")
    cursor.execute(query)
    movies=cursor.fetchall()
    cnx.close()
    return render_template('listmovies.html', movies=movies)
	
@app.route('/addmovie')
def addMovie():
    return render_template('addmovie.html')

@app.route('/submitmovie', methods=["POST"])
def submitMovie():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO Movie (MovieName, MovieYear) "
        "VALUES (%s, %s)"
    )
    data = (request.form['MovieName'], request.form['MovieYear'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
	
    return addMovie()
	
@app.route('/deletemovie')
def deleteMovie():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT * FROM Movie ORDER BY MovieName" )
    cursor.execute(query)
    movies=cursor.fetchall()
    cnx.close()
	
    return render_template('deletemovie.html', movies=movies)

@app.route('/removemovie', methods=["POST"])
def removeMovie():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    delete_stmt = (
    "DELETE FROM Movie WHERE MovieName = %s AND MovieYear = %s AND idMovie = %s")
    data = (request.form['MovieName'], request.form['MovieYear'], request.form['idMovie'])
    cursor.execute(delete_stmt, data)
    cnx.commit()
    cnx.close()
	
    return deleteMovie()
	
@app.route("/editmovie")
def editMovie():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	query = ("SELECT * FROM Movie ORDER BY MovieName" )
	cursor.execute(query)
	movies=cursor.fetchall()
	cnx.close()
	
	return render_template('editmovie.html', movies=movies)

@app.route("/updatemovie", methods=["POST"])	
def updateMovie():
    idMovie = request.form['idMovie']
    MovieName = request.form['MovieName']
    MovieYear = request.form['MovieYear']
    
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    update_stmt = ("UPDATE Movie SET MovieName = %s , MovieYear = %s WHERE idMovie = " + str(idMovie) + "")
    data = (MovieName, MovieYear)
    print("Attempting: " + update_stmt)
    cursor.execute(update_stmt, data)
    cnx.commit()
    cnx.close()
	
    return editMovie()