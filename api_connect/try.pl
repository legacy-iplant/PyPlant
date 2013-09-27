#!/bin/env perl
use strict;
use warnings;

use LWP;
use MIME::Base64;
use HTTP::Request::Common qw(POST);

my $dustin = LWP::UserAgent->new;
$dustin->timeout(10);

my $response = $dustin->get('http://dustinlanders.net');

if ($response->is_success) {
	print $response->decoded_content;
}
else {
	print $response->status_line;
}