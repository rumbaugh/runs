#! /usr/bin/perl
BEGIN { push @INC, qw[ /home/rumbaugh/Math/Math-Interpolate-1.05/lib/] }
use Math::Interpolate qw(derivatives constant_interpolate linear_interpolate robust_interpolate);

$usage = "usage: $0 source_list_radec vigcor_img asol_file outfile\n";

$srclist = shift(@ARGV) || die $usage;    # list of sky positions (ra,dec)
$vigcorimg = shift(@ARGV) || die $usage;  # vignette corrected image
$asol = shift(@ARGV) || die $usage;       # asol file
$outfile = shift(@ARGV) || die $usage; 


print STDERR "\n## Reading Catalog: $srclist\n";
@targets = split("\n", `cat $srclist`);
$n = scalar(@targets);
print STDERR "# Read $n sources\n";

open(ofile, ">>$outfile");

print STDERR "\n## Creating aperture & background region files\n";
foreach $target (@targets) {

    # Get RA, Dec
    ($ra, $dec) = split(' ', $target);
    # Create unique source id (for hash array)
    chop($rahms = `decimaltohms $ra`);
    chop($decdms = `decimaltodms $dec`);
    $sourceid = "$rahms+$decdms";           
    
    # Store source properties in hash
    $source{$sourceid}{"ra"} = $ra;
    $source{$sourceid}{"dec"} = $dec;

    # Get off-axis angle of source
    print STDERR "dmcoords $vigcorimg opt=cel ra=$ra dec=$dec asolfile=$asol\n";
    echosys("punlearn dmcoords");
    echosys("dmcoords $vigcorimg opt=cel ra=$ra dec=$dec asolfile=$asol");
    chop($x = `pget dmcoords x`);
    chop($y = `pget dmcoords y`);
    chop($theta = `pget dmcoords theta`);

    print ofile "$ra $dec $x $y $theta\n";
}


warn "\n\n# $0 : Script Complete!\n\n";

sub echosys {
        warn ("# ", $_[0], "\n");
        system($_[0]) && die "$0 : system call ($_[0]) failed\n";
}

