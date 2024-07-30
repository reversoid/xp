/*
  Warnings:

  - You are about to drop the `experiment_views` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE "experiment_views" DROP CONSTRAINT "experiment_views_experiment_id_fkey";

-- DropTable
DROP TABLE "experiment_views";
