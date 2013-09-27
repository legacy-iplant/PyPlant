#!/bin/env perl
use strict;
use warnings;

use LWP;
use MIME::Base64;
use HTTP::Request::Common qw(POST);
#use JSON::XS;

my $dustin = LWP::UserAgent->new;
#print $dustin;

#$dustin->agent("iPlant.Robot/0.1");
$dustin->agent("MyApp/0.1 ");
$dustin->default_header( Authorization => 'Basic ' . encode_base64("landersda:9fc7da9d9eda3f71ed4328bb2a4caec3") );

my $req = HTTP::Request->new(POST => 'http://dustinlanders.net');
$req->content_type('application/x-www-form-urlencoded');
$req->content('query=libwww-perl&mode=dist');

my $res = $dustin->request($req);

# Check the outcome of the response
if ($res->is_success) {
	#print "success, yay!!!! \n"
    print $res->content, "\n";
}
else {
    #print $res->status_line, "\n";
    print "that really sucks..."
}