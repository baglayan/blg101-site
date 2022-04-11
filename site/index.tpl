<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <title>Fictional developer portfolio of Chirem Nayalab</title>
        <meta name="description" content="Welcome to my portfolio. You will not be disappointed.">
        <link rel="stylesheet" type="text/css" href="https://itu-itis-2019.github.io/assignment1-ituitis-baglayan19/assignment2files/style.css" />
        <link rel="icon" href="https://itu-itis-2019.github.io/assignment1-ituitis-baglayan19/images/moonstrucklogo.png">
    </head>
    <body>
        <div class="wrapper">
            <div class="pagecontents">
                <header id="topwarning">Your ip address is: {{current_ip_address}}</header>
                <div class="topbar">
                    <q>If we're gonna be playing games, I'm gonna need a bottle of Fuse Tea Ice Tea with peach flavor.</q>
                    <ul style="text-align: right">
                        <li><a href="/">home</a></li>
                        <li><a href="/photos">photos</a></li>
                        <li><a href="/about">about</a></li>
                    </ul>
                </div>
                <br>
                <p></p>
                <div class="entiretext">
                    <div class="name">
                        <h1>Chirem Nayalab</h1>
                        <h2>Game Engine Programmer</h2>
                        <p>Welcome to my portfolio.</p>
                    </div>
                    <div class="listcontainer">
                        <h3>Portfolio:</h3>
                        <ul>
                            <li>
                                Career before games:
                                <ul>
                                    <li>Lockheed Martin</li>
                                    <li>CERN</li>
                                </ul>
                            </li>
                            <li>
                                Games I worked on:
                                <ul>
                                    <li>Hardcore Russian Fighter 2</li>
                                    <li>T.O.I.R.</li>
                                    <li> The Demise of David the Black</li>
                                </ul>
                            </li>
                        </ul>
                    </div>
                </div>
                <table>
                    <thead>
                        <tr>
                            <th>IP address</th>
                            <th>Visit count</th>
                        </tr>
                    </thead>
                    <tbody>
                        %for cia in address_dict:
                        <tr>
                            <td>{{cia}}</td>
                            <td>{{address_dict[cia]}}</td>
                        </tr>
                        %end
                    </tbody>
                </table>
                <form action="/" method="POST">
                    <input type="password" name="password" required>
                    <input class="button" value="Reset" type="submit">
                </form>

                <div class="survey">
                    <form action="/response" method="POST">
                        <p>What's your opinion on the site?</p><br>
                        <input type="radio" name="rating" value="positive">I like it<br>
                        <input type="radio" name="rating" value="negative">I hate it<br>
                        <input type="radio" name="rating" value="neutral">I don't know
                        <input class="button" value="Submit" type="submit">
                    </form>
                </div>
            </div>

            <div class="footer">
                <h3 id="contact">Contact:</h3>
                <p>Moonstruck Studios, room 1337</p>
                <p>Phone: +1345 322 456 1773</p>
                <div id="svglogocontainer">
                    <img id="footerlogo" src="https://itu-itis-2019.github.io/assignment1-ituitis-baglayan19/images/moonstrucklogo.svg" alt="Moonstruck Entertainment">
                </div>
            </div>
        </div>
    </body>
</html>