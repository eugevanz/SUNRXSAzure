
# import zeep
# from zeep import xsd

# wsdl = 'http://nlwremrvq01.mtn.co.za:8080/arsys/WSDL/public/nlaremrvq01.mtn.co.za/MWE_MTN_PMC_GET_INCIDENT_DATA?wsdl'
# client = zeep.Client(wsdl=wsdl)

# def auth():
#     username = xsd.Element('userName', xsd.String())
#     password = xsd.Element('password', xsd.String())
#     return xsd.ComplexType([username, password])

# header = xsd.Element('AuthenticationInfo', auth())
# header_value = header(userName='174877', password='mtn123')

# try:
#     response = client.service.Get_Incident_Data(Qualification="'Incident Number' = \"?\"", startRecord="", maxLimit="", _soapheaders=[header_value])
#     print('Successful response')
#     print(response)
# except Exception as e:
#     print('Error response')
#     print(e)
