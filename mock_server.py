#!/usr/bin/env python
# Basic server to do testing

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser

class RequestHandler(BaseHTTPRequestHandler):


    def print_request(self, type='GET'):

        print '*{} Request*'.format(type)
        print 'Request path is {}'.format(self.path)
        print 'Headers are {}'.format(str(self.headers))
        
    def send_resp(self, status_code=200):
        self.send_response(status_code)
 
    def do_GET(self):
        
        self.print_request(type='GET') 
        self.send_resp(200)
        
    def do_POST(self):
        
        self.print_request(type='POST') 
        self.send_resp(200)
        
        request_headers = self.headers
        content_length = request_headers.getheaders('content-length')
        length = int(content_length[0]) if content_length else 0
        
        print 'Body contents are {}'.format(self.rfile.read(length))
        

    
    do_PUT = do_POST
    do_DELETE = do_GET
        
def main(port=8080):

    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        import sys
        print 'bye'
        sys.exit(0)

        
if __name__ == "__main__":
    parser = OptionParser()
    parser.usage = '/mock_server.py [<port>]'
    (options, args) = parser.parse_args()
    if args:
        try:
    	    main(int(args[0]))
        except TypeError:
            print 'Port is not an integer'
    else:
        main()
