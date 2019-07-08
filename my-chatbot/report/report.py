import cherrypy
import os


class SurveyResult(object):
    @cherrypy.expose
    def index(self, name=None, result=None):
        return open("report.html").read().format(name=name, result=result)


conf = {'/report.css': {
    'tools.staticfile.on': True,
    'tools.staticfile.filename': os.path.abspath("./report.css"),
}}


if __name__ == '__main__':
    cherrypy.quickstart(SurveyResult(), config=conf)
