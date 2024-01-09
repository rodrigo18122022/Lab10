#!"C:\xampp\perl\bin\perl.exe"
use strict;
use warnings;
use CGI;
use DBI;
my $user = 'root';
my $password = 'payasitos';
my $dsn = "DBI:mysql:database=nuevoescritor;host=localhost;port=3307";
my $dbh = DBI->connect($dsn, $user, $password) or die("No se pudo conectar!");;
#Consultas al SGBD

$dbh->disconnect;

my $actor_id = 13;

my $busqueda = "SELECT Name FROM actor WHERE ActorId = ?";
my $sth = $dbh->prepare($busqueda);
$sth->execute($actor_id);
my ($nombre) = $sth->fetchrow_array;

if (defined $nombre) {
    print "El nombre del actor con ID 13 es: $nombre\n";
} else {
    print "No se encontro un actor con ID 13.\n";
}

$sth->finish;

