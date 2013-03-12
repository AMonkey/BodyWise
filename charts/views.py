from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import *
from django.views.generic import View
from records.models import WeightMeasurement
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as pyplt
import matplotlib.dates as mpldate
import numpy
import logging
import base64
from django.utils import simplejson as json
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

logger = logging.getLogger('term')

def getCoordinatesFromFigure(ax, fig, pts):
    #logger.debug(str(pts))
    (dates, vals) = pts.get_data()
    x = mpldate.date2num(dates)
    # normalize
    x = [(a - x[0]) / (x[-1] - x[0]) for a in x]
    vals = [(a - vals[0]) / (vals[-1] - vals[0]) for a in vals]

    #logger.debug(str(x))
    xy_pixels = [ax.transAxes.transform(a) for a in zip(x, vals)]

    #logger.debug(str(xy_pixels))

#    width, height = fig.canvas.get_width_height()
#    ypix = height - ypix

    return ([ [x.tolist()[0], x.tolist()[1]] for x in xy_pixels ])

class Grapher(View):
    def get(self, request):
        objs = WeightMeasurement.objects.order_by('time_measured').all()

        # Grab all weight values
        #dates = [x.time_measured for x in objs]
        #weights = [x.value for x in objs]

        # Far easier version, make dict
        logger.info('Creating dictionary for chart...')
        nodes = [[x.time_measured.isoformat(' '), x.value] for x in objs]
        logger.info(str(nodes))
        resp_d = {'nodes': nodes}

        ## MAke chart (it's ugly ksry)
        #fig = pyplt.figure()
        #ax = fig.add_subplot(111)
        #points, = ax.plot(dates, weights, 'ro-')
        #fig.autofmt_xdate()

        ## Calculate pixel coords
        ##pxs = []
        #pxs = getCoordinatesFromFigure(ax, fig, points)
        #logger.info('Coordinates for image are: ' + str(pxs))

        ## Print graph to b64 png
        #img_buffer = StringIO()
        #canvas = FigureCanvasAgg(fig)
        #canvas.print_png(img_buffer)
        #img_buffer.seek(0)
        #img_str = base64.b64encode(img_buffer.getvalue())

        # Make dictionary
        #(width, height) = canvas.get_width_height()
        #resp_d = {'nodes': pxs, 'img_width': width,
        #    'img_height': height}
        logger.info('Sending JSON dictionary: %s' % json.dumps(resp_d))

        return HttpResponse(json.dumps(resp_d), content_type='application/json')
        
