extern crate heck;
use heck::SnakeCase;
use std::io;
use std::io::prelude::*;

fn main() {
    for line in io::stdin().lock().lines() {
        println!("{}", line.unwrap().to_snake_case());
    }
}
