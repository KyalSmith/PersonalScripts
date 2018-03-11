import subprocess
import json


def Get_IDs():

    app_ids = {}

    output = subprocess.check_output("curl -H \"x-api-key:b5bbcfadce5418c83069df1047f3f978c8e5d14a2a3838f\" -X GET \'https://api.newrelic.com/v2/applications.json\' ",shell=True)

    output = output.decode()

    output = json.loads(output)


    for val in output['applications']:

        for item in val:

            app_ids[val['id']]=val['name']

    print("\n\nApplication_ID\tApplication_Name:\n---------------------------------")

    for item in app_ids:

        print(str(item)+":\t"+str(app_ids[item]))

        

if __name__=="__main__":
    Get_IDs()
