from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import *
from django.views.generic import View, TemplateView
#import constants # not sure this is the way to do this?

from records.models import Record, WeightMeasurement
import time
import datetime
import logging
import constants
import json

# Make a fuckin logger ok?
logger = logging.getLogger('term')

class Index(TemplateView):
    template_name = 'records/index.html'

    def get(self, request):
        return self.render_to_response({})

class Submit(View):
    def get(self, request):
        data = {'sub_recs': (x[0] for x in constants.SUBRECORDS)}
        template_name = 'records/submit_record.html'
        # I also think there is a better way to do this, with defaults maybe?
        if request.GET.has_key('selected_template'):
            # This is the AJAX request part woo
            template_name = request.GET['selected_template']

        else:
            data['parts'] = constants.PARTS # Better to not include?
            data['lifts'] = constants.LIFTS

        return render(request, template_name, data)

    def post(self, request):
        # Iff you can't do it pretty, do it ugly. My god I am sorry.
        # https://docs.djangoproject.com/en/dev/ref/models/instances/#django.db.models.Model
        data = json.loads(request.raw_post_data)
        logging.warning("Post contains: %s" % str(data))
        record = Record(user='foo')
        record.save()

        # Begin the for loop of death
        metric_type = data.keys()
        logging.warning('Keys are: %s' % metric_type)
        for m in metric_type:
            logging.warning(m)
            if m is None:
                return redirect('/')
            
            if m == 'Weight':
                logging.warning("Creating weight record")
                value = data[m]['value']
                time_measured = data[m]['time_measured']

                if all([value, time_measured]):
                    time_measured = datetime.datetime.strptime(time_measured, '%m/%d/%Y')
                    metric = WeightMeasurement(record=record,
                                               value=value,
                                               time_measured=time_measured)
                    metric.save()
                    return redirect('/')
  
            if m == 'Body Fat':
                value = data[m].get('value', None)
                time_measured = data[m].get('time_measured', None)

                if all([value, time_measured]):
                    metric = BodyFatMeasurement(record=record,
                                                value=value,
                                                time_measured=time_measured)
                    metric.save()
                    return redirect('/')

            if m == 'Body Size':
                value = data[m].get('value', None)
                time_measured = data[m].get('time_measured', None)
                body_part = data[m].get('body_part', None)
                

                if all([value, time_measured, body_part]):
                    metric = BodyFatMeasurement(record=record,
                                                value=value,
                                                body_part=body_part,
                                                time_measured=time_measured)
                    metric.save()
                    return redirect('/')
                 
            if m == 'Max Lift':
                value = data[m].get('value', None)
                time_measured = data[m].get('time_measured', None)
                lift = request.POST[m].get('lift', None) 

                if all([value, time_measured, lift]):
                    metric = MaxLiftMeasurement(record=record,
                                                value=value,
                                                lift=lift,
                                                time_measured=time_measured)
                    metric.save()
                    return redirect('/')

            if m == 'Resting Heart Rate':
                value = request.POST[m].get('value', None)
                time_measured = request.POST[m].get('time_measured', None)

                if all([value, time_measured]):
                    metric = RestingHRMeasurement(record=record,
                                                  value=value,
                                                  time_measured=time_measured)
                    metric.save()
                    return redirect('/')

            if m == 'Sleep':
                hours = request.POST[m].get('value', None)
                time_measured = request.POST[m].get('time_measured', None)
                quality = request.Post.POST[m].get('quality', None)

                if all([time_measured, hours, quality]):
                    metric = SleepMeasurement(record=record,
                                              hours=hours,
                                              quality=quality,
                                              time_measured=time_measured)
                    metric.save()
                    return redirect('/')

            else:
                return redirect('/')

