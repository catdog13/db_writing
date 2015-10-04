import dataset
import cherrypy
db = dataset.connect('sqlite:///C:\\Users\\Tom\Documents\\Python_Projects\\db_writing\\db_files\\video_list.db')


class MainRun(object):
    @cherrypy.expose
    def index(self):
        return 'Why are you here'

    def make_list(self, sort):
        body = ["""<html>
                <head>
                <style>
                    table, td, th {
                        border-collapse: collapse;
                        border: 1px solid black;
                        padding: 3px;
                        }
                </style>
                </head>
                <body>
                <table border="1">
                <tr>
                <th>movie_name</th>
                <th>status</th>
                <th>imdb_id</th>
                <th>mpaa_rating</th>
                <th>tomato_rating</th>
                <th>imdb_rating</th>
                <th>genre</th>
                <th>release_date</th>
                <th>plot</th>
                <th>runtime</th>
                <th>file_size</th>
                <th>path</th>
                <th>actors</th>
                </tr>"""]
        result = db.query('SELECT * FROM Movies ORDER BY ' + sort)
        for row in result:
            new_row = """<tr>
                         <td>""" + row['movie_name'] + """</td>
                         <td>""" + row['status'] + """</td>
                         <td>""" + row['imdb_id'] + """</td>
                         <td>""" + row['mpaa_rating'] + """</td>
                         <td>""" + row['tomato_rating'] + """</td>
                         <td>""" + row['imdb_rating'] + """</td>
                         <td>""" + row['genre'] + """</td>
                         <td>""" + row['release_date'] + """</td>
                         <td>""" + row['plot'] + """</td>
                         <td>""" + row['runtime'] + """</td>
                         <td>""" + row['file_size'] + """</td>
                         <td>""" + row['path'] + """</td>
                         <td>""" + row['actors'] + """</td>
                         </tr>"""
            body.append(new_row)
        body.append('</table></body></html>')
        return body

    @cherrypy.expose
    def name(self):
        func = self.make_list('movie_name')
        return func

    @cherrypy.expose
    def id(self):
        func = self.make_list('_rowid_')
        return func

    @cherrypy.expose
    def status(self):
        func = self.make_list('status')
        return func

if __name__ == '__main__':
    cherrypy.server.socket_host = '192.168.1.21'
    cherrypy.server.socket_port = 8080
    cherrypy.quickstart(MainRun(), '/movies')
