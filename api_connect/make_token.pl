#!/bin/env perl
use LWP;
use MIME::Base64;
$ua = LWP::UserAgent->new;
$ua->agent("iPlant.Robot/0.1");
$ua->default_header( Authorization => 'Basic '.encode_base64("landersda:Shadow@3876") );
$req = HTTP::Request->new(POST => "https://foundation.iplantc.org/auth-v1/");
$res = $ua->request($req);
if ($res->is_success) {
	print $res->decoded_content;
    print STDERR "Token recieved\n";
} else {
    print STDERR $res->status_line, "\n";
}