#!/bin/env perl
use LWP;
use MIME::Base64;
$ua = LWP::UserAgent->new;
$ua->agent("iPlant.Robot/0.1");
$ua->default_header( Authorization => encode_base64("landersda:39f668f71c9ab23656b53c5d1eceb380") );
$req = HTTP::Request->new(DELETE => "https://foundation.iplantc.org/auth-v1/");
$res = $ua->request($req);
if ($res->is_success) {
    print STDERR "Token deleted\n";
} else {
    print STDERR $res->status_line, "\n";
}