var autoprefixer            = require("autoprefixer");
var browserSync             = require("browser-sync").create();
var del                     = require("del");
var gulp                    = require("gulp");
var cleanCSS                = require("gulp-clean-css");
var concatJs                = require("gulp-concat");
var concatCss               = require("gulp-concat-css");
var git                     = require("gulp-git");
var googleWebFonts          = require("gulp-google-webfonts");
var cp                      = require("child_process");//jekyll
var imagemin                = require("gulp-imagemin");
var notify                  = require("gulp-notify");
var plumber                 = require("gulp-plumber");
var postcss                 = require("gulp-postcss");
var shell                   = require("gulp-shell");
var sourcemaps              = require("gulp-sourcemaps");
var stylus                  = require("gulp-stylus");
var lost                    = require("lost");
var rsync                   = require("rsyncwrapper");
var runSequence             = require("run-sequence");
var rupture                 = require("rupture");

//--------------------------------------------------------------

var fs                      = require("fs");
var varsProject             = JSON.parse(fs.readFileSync("./vars-project.json"));
var dominio                 = varsProject.dominio;
var url                     = "https://" + varsProject.dominio;
var diplenick               = varsProject.diplenick;
var options                 = { }; //webfonts

//---------------------------------------------------------FONTS

gulp.task("fonts", function(callback) {
    runSequence(
        "font-del",
        "webfonts",
        callback
        )
});

gulp.task("font-del", function() {
    del("fonts")
});

gulp.task("webfonts", function () {
    return gulp.src("fonts.list")
    .pipe(googleWebFonts(options))
    .pipe(gulp.dest("fonts"))
});

//-----------------------------------------------------------CSS

gulp.task("stylus", function() {
    return gulp.src("_src/styl/style.styl")
    .pipe(plumber({errorHandler: notify.onError({
        message: "Error: <%= error.message %>",
        title: "Erro na tarefa Stylus"
    })}))
    .pipe(sourcemaps.init())
    .pipe(stylus({
        use:[rupture()],
    }))
    .pipe(postcss([
        lost(),
        autoprefixer()
        ]))
    .pipe(sourcemaps.write())
    .pipe(gulp.dest("app/static/assets/css/"))
    .pipe(browserSync.stream())
});

// gulp.task("third-css", function() {
//     return gulp.src("assets/third/**/*.css")
//     .pipe(concatCss("third.css"))
//     .pipe(gulp.dest("assets/css/"))
// });

// gulp.task("min-css", function() {
//     return gulp.src("_site/assets/css/*.css")
//     .pipe(cleanCSS())
//     .pipe(gulp.dest("_site/assets/css/"))
// });

//------------------------------------------------------------JS

gulp.task("js", function() {
    rsync({
        src: "_src/js/script.js",
        dest: "app/static/assets/js/script.js",
        recursive: true,
        args: [ "-v" ],
        delete: true,
        compareMode: "checksum",
        onStdout: function (data) {
            console.log(data.toString());
        }
    }, function() {
        console.log("End")
    });
});

// gulp.task("third-js", function() {
//     return gulp.src("_src/third/**/*.js")
//     .pipe(concatJs("third.js"))
//     .pipe(gulp.dest("assets/js/"))
// });

//--------------------------------------------------------------

gulp.task("browser-sync", function() {
    browserSync.init({
        proxy: "localhost:8000",
        open: false
    });
});

gulp.task("browserSync-reload", function() {
    browserSync.reload()
});

//--------------------------------------------------------------

gulp.task("sync-favicon", function() {
    rsync({
        src: ["_src/favicon/"],
        dest: "assets/favicon/",
        recursive: true,
        args: ["-v"],
        delete: true,
        compareMode: "checksum",
        onStdout: function (data) {
            console.log(data.toString());
        }
    }, function() {
        console.log("End");
    });
});

gulp.task("sync-img", function() {
    rsync({
        src: ["_src/img"],
        dest: "assets/",
        recursive: true,
        args: ["-v"],
        delete: true,
        compareMode: "checksum",
        onStdout: function (data) {
            console.log(data.toString());
        }
    }, function() {
        console.log("End ");
    });
});

gulp.task("min-image", function() {
    return gulp.src("_src/img/*.*")
    .pipe(imagemin())
    .pipe(gulp.dest("assets/img/"))
});

//--------------------------------------------------------------

gulp.task("git-add", function() {
    return gulp.src("./")
    .pipe(git.add({args: "-A"}));
});

gulp.task("git-commit", function() {
    return gulp.src("./")
    .pipe(git.commit("Commit"));
});

gulp.task("git-push", function() {
    git.push("origin", "master", function (err) {
        if (err) throw err;
    });
});

//--------------------------------------------------------------

gulp.task("watch", function () {
    gulp.watch(["app/templates/*.html"]).on("change", browserSync.reload);
    gulp.watch(["_src/styl/**/*.styl"], ["stylus"]).on("change", browserSync.reload);
    gulp.watch(["_src/js/*.js"], ["js"]).on("change", browserSync.reload);
});

//--------------------------------------------------------------

//F7
gulp.task("deploy", function(callback) {
    runSequence(
        "git-add",
        "git-commit",
        "git-push",
        callback
        );
});

//F9
gulp.task("letscode", function(callback) {
    runSequence(
        "browser-sync",
        "watch",
        callback
        );
});
